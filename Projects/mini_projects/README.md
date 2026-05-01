# 🌍 Project Greenland: Geophysical Research Pipeline
### *M.Sc. Applied Geophysics | University of Ibadan*

## 📌 Overview
This repository serves as the computational foundation for my research on groundwater and aquifer characterization in Ibadan, Oyo State. It integrates fundamental linear algebra with automated literature surveying.

## 🛠 Features

### 1. Gaussian Elimination Solver (Python Edition)
Implements the core mathematical logic for solving $3 \times 3$ systems of linear equations.
* **Zero-Pivot Handling**: Manages potential division-by-zero errors during matrix reduction.
* **System Diagnostics**: Identifies Independent, Dependent, or Inconsistent systems.
* **Back Substitution**: Solves for variables once Row Echelon Form is achieved.

### 2. Geophysical Journal Scout
An automated tool designed to build a database of regional geophysical studies.
* **Automated Surveying**: Uses the `scholarly` library to query Google Scholar.
* **Categorized Output**: Organizes literature into CSV files for 1D VES, 2D ERT, Technical methods, and Localized studies (Akinyele, Iddo LGAs).
* **Metadata Export**: Captures titles, authors, and direct publication links.

## 🚀 How to Run
Ensure you have Python 3.x and the Anaconda environment installed.

### For the Gaussian Solver:
```bash
python3 gaussian_interactive.py
python3 gaussian_phy781.py
python3 journalscript.py
