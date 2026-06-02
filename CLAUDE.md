# CLAUDE.md

Python reimplementations of exercises from **_Analyzing Neural Time Series Data: Theory and Practice_** (Mike X Cohen, MIT Press 2014). The book ships MATLAB code; this repo ports the exercises to Python. Public learning / portfolio repo.

## Environment
A project virtualenv lives at `.venv/` (git-ignored). **Activate it before running any Python** — `source .venv/bin/activate`, or invoke `.venv/bin/python` directly. Pinned deps are in `requirements.txt` (`pip install -r requirements.txt`) — currently `numpy` + `matplotlib`.

## Stack
- Scientific Python: `numpy`, `scipy`, `matplotlib`.
- `mne` (MNE-Python) for EEG-specific routines where it helps.
- Notebooks (`.ipynb`) and/or plain scripts — not pinned yet.

## Conventions
- This is a **learning** repo: prefer clear, explicit, well-commented code that mirrors the book's steps over terse/optimized one-liners. Readability > cleverness.
- **Python only — never write or suggest MATLAB.** The book's code is MATLAB; we read it but reimplement everything in Python.
- **Display & plotting:** `matplotlib` is the approved tool for all image/plotting exercises (`imshow`, subplots, etc.).
- Organize by chapter as exercises get added (e.g. `ch4/`, `ch5/`).

## Porting gotchas (MATLAB → Python)
- MATLAB is 1-indexed, Python 0-indexed — watch off-by-one in time/channel indexing.
- MATLAB ranges `a:b` are inclusive of `b`; Python `a:b` excludes `b`. MATLAB `end` → Python `-1`.
- MATLAB is column-major; numpy defaults to row-major (C-order) — mind axis order when vectorizing.
- Sample `.mat` data loads via `scipy.io.loadmat` (or `mne` for EEG containers). Large data files are git-ignored — keep them out of commits.
