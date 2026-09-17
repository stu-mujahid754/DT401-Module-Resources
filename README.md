# DT401 Module Resources - Data Fundamentals

Welcome to the DT401 Module Resources repository. This collection of interactive Jupyter notebooks provides hands-on training in data fundamentals, from basic data concepts through advanced analysis techniques.

## What's Inside

This repository contains **19 interactive Jupyter notebooks** organised across 7 weeks of content, covering:

- **Week 1:** Data fundamentals, SQL databases, and data formats (CSV/JSON)
- **Week 2:** Python data types, structures, and working with data formats
- **Week 3:** Data quality assessment, lifecycle management, and data integration
- **Week 4:** Data gathering methods, relationships, and descriptive statistics
- **Week 5:** Complete data analysis lifecycle, regression, clustering, and hypothesis testing
- **Week 6:** Data anonymisation and privacy protection techniques
- **Week 7:** Advanced time-series analysis, forecasting, and complete projects

## Learning Objectives

By completing these notebooks, you will:
- Understand fundamental data concepts and structures
- Work with SQL databases and multiple data formats
- Assess and improve data quality
- Perform exploratory data analysis and statistical testing
- Build regression and clustering models
- Implement data anonymisation for privacy compliance
- Create forecasts using time-series analysis
- Apply the complete data analysis lifecycle to real problems

## Getting Started

### All in the Browser - No Downloads Needed

#### Step 1: Create Your Own Copy from the Template

1. **Go to the GitHub repository**
   - Open the repository link in your browser

2. **Click the green "Use this template" button**
   - It's near the top of the repository, next to the **Code** button
   - Select **Create a new repository** from the dropdown

3. **Configure your new repository**
   - Choose your own GitHub account as the **Owner**
   - Enter a name for your repository
   - Set the visibility to **Private**. Your reflections will contain your own workplace examples and personal notes, so this repository should not be public
   - Leave "Include all branches" unchecked; you only need the default branch

4. **Click "Create repository"**
   - GitHub creates a complete, independent copy in your account within a few seconds

Now you have your own copy of the repository.

#### Step 2: Open in GitHub Codespaces

5. **Go to your new repository**
   - Navigate to the repository you just created in your account

6. **Click the green Code button**
   - Look for the green **Code** button

7. **Select the Codespaces tab**
   - Click on the **Codespaces** tab

8. **Click "Create codespace on main"**
    - This creates your personal cloud development environment

9. **Wait for setup (2-3 minutes)**
    - The system automatically:
      - Installs Python 3.12
      - Installs all required packages from `requirements.txt`
      - Configures Jupyter environment
      - Installs VS Code extensions

10. **Start Jupyter**
    - Open the terminal in your Codespace
    - Run: `jupyter notebook`
    - Click the forwarded URL to access Jupyter

That's it. No installations, no downloads, no command line knowledge needed. Everything runs in your browser.

**Note:** Codespaces provides the best learning experience with everything pre-configured. This is the recommended way to learn with these notebooks.

## How to Use These Notebooks

### Navigation
Each week has multiple sections (e.g., `DT401_Week1_Section1.ipynb`):
- Start with **Section 1** of each week
- Complete sections sequentially for best learning outcomes
- Each notebook builds on concepts from previous ones

### Working Through a Notebook

1. **Read the context** - Each section starts with business scenarios and learning objectives
2. **Execute code cells** - Run each code cell (Shift+Enter) to see outputs
3. **Modify and experiment** - Change values, explore different approaches
4. **Complete tasks** - Many notebooks include hands-on tasks and reflections
5. **Save your work** - Use Ctrl+S to save progress

### Dataset
Most examples use weather data from the **Open-Meteo API** (London, UK, 2023-2026). This data is included as `open-meteo-51.49N0.16W23m.csv` in the root directory.

## Required Packages

All packages are automatically installed via `requirements.txt`:

- **Data Processing:** pandas, numpy
- **Visualisation:** matplotlib, seaborn, plotly
- **Analysis:** scipy, scikit-learn, statsmodels
- **Privacy:** anonympy
- **Notebooks:** jupyter, notebook, ipykernel

See `requirements.txt` for specific versions.

## Development Environment

### VS Code Extensions (Auto-Installed in Codespace)
- Python + Pylance (`ms-python.python`)
- Jupyter (`ms-toolsai.jupyter`)
- Data Wrangler (`ms-toolsai.datawrangler`)
- Markdown Mermaid (`bierner.markdown-mermaid`)

### Codespace Settings
The Codespace is pre-configured with:
- Python interpreter pointed to the Python 3.12 environment
- Jupyter notebooks open relative to the workspace root

## Content Overview

| Week | Topics | Time |
|------|--------|------|
| 1 | Data fundamentals, SQL, CSV/JSON | 2.5 hrs |
| 2 | Python types, structures, formats | 3 hrs |
| 3 | Data quality, lifecycle, integration | 3 hrs |
| 4 | Data gathering, statistics, correlation | 2.5 hrs |
| 5 | Analysis lifecycle, modelling, hypothesis testing | 3 hrs |
| 6 | Data anonymisation & privacy | 1.5 hrs |
| 7 | Time-series, forecasting, projects | 2.5 hrs |

**Total:** ~18 hours of interactive learning

## Portfolio Evidence

Each week's notebooks include:
- Hands-on activities (`DT401_WeekX_hands_on_todo.md`)
- Independent tasks for portfolio development
- Real-world business scenarios
- Reflection prompts for professional development

## How Your Reflections Are Compiled

Most notebook sections end with a `## Reflection` block: a short set of questions, followed by a markdown cell starting with *"Your reflections here..."*. Write your answers into that cell in place of the placeholder text (keep the numbering if it's there) and save the notebook as normal.

Every time you push a commit, a GitHub Action automatically:

1. Reads any Week notebook you changed and checks whether its `## Reflection` cell has been filled in (an untouched placeholder is skipped, not treated as an answer).
2. Compiles completed reflections for that week, with the questions and your answers together, into `reflections_Week_<n>.md` inside that week's folder.
3. Rebuilds a single `module_reflections.md` at the root of the repository, combining every week that has at least one completed reflection.

You don't need to run anything yourself. These files appear and update automatically after you push. They exist so your coach can review your reflections in one place without opening every notebook individually. Sections you haven't answered yet simply don't appear, so there's no placeholder clutter to review.

## Sharing Access with Your Coach

You were instructed above to set your repository's visibility to **Private**. If you did, nobody else, including your coach, can see it by default, even though the compiled reflection files are being updated automatically. You need to explicitly invite your coach as a collaborator:

1. Go to your repository on GitHub
2. Click **Settings**
3. Select **Collaborators and teams** in the left sidebar (you may be asked to confirm your password)
4. Click **Add people**
5. Enter your coach's GitHub username or email address and send the invite

Your coach will need to accept the invitation before they can see your repository, so send this early rather than just before a review is due. If you're not sure whether your repository is currently private, check under **Settings → General → Danger Zone**, where you can also change it if needed.

## Troubleshooting

### Codespace Issues
- **Environment slow to build?** - Normal for first build (2-3 min). Subsequent launches are faster.
- **Packages not installing?** - Check internet connection. Manual installation: `pip install -r requirements.txt`
- **Jupyter not starting?** - Ensure port 8888 is available. Try: `jupyter notebook --port 8889`

### Notebook Issues
- **Kernel crashes?** - Restart kernel: Kernel → Restart
- **Missing data file?** - Ensure `open-meteo-51.49N0.16W23m.csv` is in root directory
- **Import errors?** - Reinstall packages: `pip install --upgrade -r requirements.txt`

## Support

- Check the **README.md** files in each week's folder for section-specific guidance
- Review **hands-on checklist** files for task guidance
- Use professional logbook for reflection and progress tracking

## License & Credits

**Dataset:** Weather data from [Open-Meteo API](https://open-meteo.com) (London, UK)

**Framework:** DT401 Continuous Improvement v4.26

## Next Steps

1. **Open a Codespace** or set up locally
2. **Start with Week 1** - Begin with `DT401_Week1_Section1.ipynb`
3. **Follow the learning path** - Complete weeks sequentially
4. **Take notes** - Use the reflection prompts in each notebook
5. **Build portfolio** - Collect evidence from independent tasks

---

Happy learning.

