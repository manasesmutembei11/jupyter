# Jupyter / Python Exercises

A personal collection of Jupyter notebooks and small Python projects that demonstrate core programming concepts, algorithms, and common exercises used for learning Python, data structures, and problem-solving.

## What you'll find here
- Beginner-to-intermediate Python exercises implemented as scripts and Jupyter notebooks.
- Small standalone projects and algorithm demonstrations (e.g., a budget category manager, arithmetic arranger, binary search tree traversal, polygon area helper, and vector math with special methods).
- Code intended for hands-on learning, experimentation, and incremental improvement.

### Stack
- **Language(s):** Jupyter Notebook (primary), Python
- **Runtime:** CPython 3.8+ (any recent Python 3 release) and Jupyter Notebook / JupyterLab
- **Typical libraries:** standard library only in most scripts (install extras if notebooks require them)

## Repository layout (top-level)
src/ (not present) — this repo keeps scripts and notebooks at the top level

Top-level files and a short description:
- *.ipynb — Several Jupyter notebooks (interactive lessons and experiments)
- arithmetic_formatter.py — Formatter for simple arithmetic problems (exercise)
- budget_app.py — Category class and spend chart generator (small budgeting exercise)
- polygon_area_calculator.py — Rectangle / Square classes with geometry helpers
- tree_traversal.py — Binary Search Tree implementation and traversal demo
- special_methods.py — Vector classes demonstrating dunder methods and operators
- other .py files (data structures, recursion, special methods, examples) — assorted training exercises

**How it fits together:** This repo is not a single application but a curated set of independent examples and learning artifacts. Each script/notebook is runnable on its own and demonstrates a specific concept or challenge.

## How to run things locally
1. Install Python (3.8+) and Jupyter:
   - Using pip:
     ```
     python -m pip install --upgrade pip
     python -m pip install jupyter
     ```
   - Or install JupyterLab:
     ```
     python -m pip install jupyterlab
     ```

2. Open notebooks:
   - From the repo root:
     ```
     jupyter notebook
     # or
     jupyter lab
     ```
   - Then open any `.ipynb` file in your browser.

3. Run standalone scripts:
   - From the repo root:
     ```
     python arithmetic_formatter.py
     python budget_app.py
     python tree_traversal.py
     ```

