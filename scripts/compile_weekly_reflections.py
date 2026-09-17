"""Compile all per-week reflections_Week_<n>.md files into one top-level module_reflections.md.

Run after scripts/extract_reflections.py has (re)generated each Week folder's
reflections_Week_<n>.md. Weeks with no reflections file (nothing filled in
yet) are skipped. Heading levels from each week file are promoted by one
level so the result nests cleanly under a single top-level title.

Usage:
    python scripts/compile_weekly_reflections.py [--check]
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from extract_reflections import week_sort_key  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
HEADING_RE = re.compile(r"^(#+)(\s+.*)$")


def promote_headings(text: str, by: int = 1) -> str:
    lines = text.split("\n")
    out = []
    for line in lines:
        match = HEADING_RE.match(line)
        if match:
            out.append("#" * (len(match.group(1)) + by) + match.group(2))
        else:
            out.append(line)
    return "\n".join(out)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check", action="store_true",
        help="report what would happen without writing or deleting files",
    )
    args = parser.parse_args()

    week_dirs = sorted(REPO_ROOT.glob("Week *"), key=week_sort_key)
    blocks = []
    for week_dir in week_dirs:
        reflection_file = week_dir / f"reflections_{week_dir.name.replace(' ', '_')}.md"
        if not reflection_file.exists():
            continue
        text = reflection_file.read_text(encoding="utf-8").strip()
        blocks.append(promote_headings(text, by=1))

    out_path = REPO_ROOT / "module_reflections.md"

    if not blocks:
        if out_path.exists():
            print(f"{'would remove' if args.check else 'removing'}: {out_path.name} (nothing filled in anywhere)")
            if not args.check:
                out_path.unlink()
        else:
            print("nothing filled in anywhere; no module_reflections.md to write")
        return

    content = "# Module Reflections\n\n" + "\n\n---\n\n".join(blocks) + "\n"
    action = "would write" if args.check else "writing"
    print(f"{action}: {out_path.name} ({len(blocks)} week(s))")
    if not args.check:
        out_path.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    sys.exit(main())
