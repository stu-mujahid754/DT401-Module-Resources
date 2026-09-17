"""Compile completed Reflection sections from each Week's notebooks into one file.

For each `Week <n>` folder, looks at every notebook inside it, finds the
markdown cell containing a "## Reflection" heading and the response cell that
follows it. Notebooks whose response cell still holds only the unfilled
placeholder are skipped.

Per FS-02 §3.10, the prompt cell carries up to four framing paragraphs
(Task, Assessment context, Referencing, Review-and-revision) before the
questions, none of which are learner-facing content worth compiling. Only
the numbered questions inside the `alert-block alert-info` div, including
any inline learning-outcome tags such as "(MLO1)", are extracted. Everything
else in the prompt cell is discarded.

The extracted questions and the learner's answer are compiled into a single
`reflections_Week_<n>.md` in that Week folder, under a level-2 heading
naming the source notebook's section (e.g. "Section_1" for
`DT401_Week_2_Section_1.ipynb`) — for coaches reviewing the work without
having to open every notebook individually.

Usage:
    python scripts/extract_reflections.py [--check] [--since REF]

--check reports what would happen without writing or deleting anything.
--since REF restricts processing to Week folders containing a notebook
changed between REF and HEAD (via `git diff --name-only`), leaving every
other week's reflections_Week_<n>.md untouched — for use in CI, where a
push usually only touches one week's notebooks and there is no need to
re-read the rest.
Without --since, every Week folder is processed, which is the right default
for a manual/local run.
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

import nbformat

REPO_ROOT = Path(__file__).resolve().parent.parent
HEADING_RE = re.compile(r"^##\s+Reflection\s*$", re.MULTILINE)
QUESTIONS_BOX_RE = re.compile(
    r'<div class="alert alert-block alert-info">(.*?)</div>', re.DOTALL
)
MLO_BULLET_LINE_RE = re.compile(r"(?m)^-\s*\*\*MLO\d+:\*\*\s*\*[^*\n]+\*\s*$")
MLO_INLINE_RE = re.compile(r"\*\*MLO\d+:\*\*\s*\*[^*\n]+\*")
PLACEHOLDER_LINE_RE = re.compile(r"(?m)^[*_]Write your responses here\.[*_]\s*$\n?")
NUMBERED_STUB_RE = re.compile(r"(?m)^\s*\d+\.\s*$\n?")
REFERENCES_LABEL_RE = re.compile(r"(?m)^References \(if applicable\):\s*$")
SECTION_LABEL_RE = re.compile(r"(Section.*)$", re.IGNORECASE)
WEEK_NUMBER_RE = re.compile(r"Week\s*(\d+)", re.IGNORECASE)


def section_label(notebook_path: Path) -> str:
    match = SECTION_LABEL_RE.search(notebook_path.stem)
    return match.group(1) if match else notebook_path.stem


def find_reflection_cells(nb):
    for i, cell in enumerate(nb.cells):
        if cell.cell_type == "markdown" and HEADING_RE.search(cell.source):
            response_cell = nb.cells[i + 1] if i + 1 < len(nb.cells) else None
            if response_cell is not None and response_cell.cell_type != "markdown":
                response_cell = None
            return cell, response_cell
    return None, None


def extract_questions(prompt_source: str):
    """The numbered questions (with any MLO tags) inside the alert-info box.

    Returns None if no alert-info box is found, e.g. a notebook not yet
    updated to the FS-02 §3.10 template — callers should skip and warn
    rather than fall back to including the framing paragraphs verbatim.
    """
    match = QUESTIONS_BOX_RE.search(prompt_source)
    return match.group(1).strip() if match else None


def extract_mlos(prompt_source: str):
    """The learning-outcome reference(s) from the Assessment context paragraph.

    Per FS-02 §3.10, multiple outcomes are listed as a bulleted
    "- **MLOx:** *wording*" line each; a single outcome is instead named
    inline within a sentence as "**MLOx:** *wording*". Returns that text
    verbatim (bullets as bullets, inline as inline), or None if the
    reflection is purely formative and names no outcome at all.
    """
    bullet_lines = MLO_BULLET_LINE_RE.findall(prompt_source)
    if bullet_lines:
        return "\n".join(line.strip() for line in bullet_lines)
    match = MLO_INLINE_RE.search(prompt_source)
    return match.group(0) if match else None


def strip_response_boilerplate(response_source: str) -> str:
    text = PLACEHOLDER_LINE_RE.sub("", response_source)
    text = NUMBERED_STUB_RE.sub("", text)
    match = REFERENCES_LABEL_RE.search(text)
    if match and not text[match.end():].strip():
        text = text[:match.start()]
    return text.strip()


def is_unfilled(response_source: str) -> bool:
    return not strip_response_boilerplate(response_source)


def build_section(notebook_path: Path, questions: str, mlos, response_cell) -> str:
    answers = strip_response_boilerplate(response_cell.source)
    parts = [f"## {section_label(notebook_path)}"]
    if mlos:
        parts.append(mlos)
    parts.append(questions)
    parts.append(f"### Responses\n\n{answers}")
    return "\n\n".join(parts)


def week_sort_key(week_dir: Path):
    match = WEEK_NUMBER_RE.search(week_dir.name)
    return int(match.group(1)) if match else week_dir.name


def changed_week_dirs(since_ref: str):
    """Week folders containing a notebook changed between since_ref and HEAD.

    Returns None (meaning "couldn't tell, caller should fall back to
    processing every week") if the ref can't be diffed, e.g. a shallow clone
    that doesn't have since_ref locally.
    """
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", since_ref, "HEAD"],
            cwd=REPO_ROOT, capture_output=True, text=True, check=True,
        )
    except subprocess.CalledProcessError as exc:
        print(f"WARNING: git diff against {since_ref!r} failed, processing all weeks: {exc.stderr.strip()}")
        return None

    names = set()
    for line in result.stdout.splitlines():
        path = Path(line)
        if path.suffix == ".ipynb" and len(path.parts) == 2 and path.parts[0].startswith("Week "):
            names.add(path.parts[0])
    return {REPO_ROOT / name for name in names}


def compile_week(week_dir: Path):
    sections = []
    for notebook_path in sorted(week_dir.glob("*.ipynb")):
        nb = nbformat.read(open(notebook_path, "r", encoding="utf-8"), as_version=4)
        prompt_cell, response_cell = find_reflection_cells(nb)
        if response_cell is None or is_unfilled(response_cell.source):
            continue
        questions = extract_questions(prompt_cell.source)
        if questions is None:
            print(
                f"WARNING: {notebook_path.relative_to(REPO_ROOT)} has a filled-in "
                "reflection but no alert-info questions box (FS-02 §3.10 format) "
                "was found; skipping it rather than guessing"
            )
            continue
        mlos = extract_mlos(prompt_cell.source)
        sections.append(build_section(notebook_path, questions, mlos, response_cell))
    return sections


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check", action="store_true",
        help="report what would happen without writing or deleting files",
    )
    parser.add_argument(
        "--since", metavar="REF",
        help="only process weeks with a notebook changed since this git ref",
    )
    args = parser.parse_args()

    if args.since:
        week_dirs = changed_week_dirs(args.since)
        if week_dirs is None:
            week_dirs = set(REPO_ROOT.glob("Week *"))
        elif not week_dirs:
            print(f"no Week notebooks changed since {args.since}; nothing to do")
        week_dirs = sorted(week_dirs, key=week_sort_key)
    else:
        week_dirs = sorted(REPO_ROOT.glob("Week *"), key=week_sort_key)

    written, removed, skipped = 0, 0, 0
    for week_dir in week_dirs:
        sections = compile_week(week_dir)
        out_path = week_dir / f"reflections_{week_dir.name.replace(' ', '_')}.md"

        if not sections:
            if out_path.exists():
                removed += 1
                print(f"{'would remove' if args.check else 'removing'}: {out_path.relative_to(REPO_ROOT)}")
                if not args.check:
                    out_path.unlink()
            else:
                skipped += 1
            continue

        content = f"# {week_dir.name} Reflections\n\n" + "\n\n---\n\n".join(sections) + "\n"
        action = "would write" if args.check else "writing"
        print(f"{action}: {out_path.relative_to(REPO_ROOT)} ({len(sections)} section(s))")
        written += 1
        if not args.check:
            out_path.write_text(content, encoding="utf-8")

    print(f"\n{written} week file(s) written, {removed} removed, {skipped} weeks with nothing filled in")


if __name__ == "__main__":
    sys.exit(main())
