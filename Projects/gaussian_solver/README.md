# Gaussian Elimination Solver - Python Edition
### *Linear Systems for Geoscience Data*

## 📌 Overview
This script implements the **Gaussian Elimination** algorithm from scratch to solve $3 \times 3$ systems of linear equations. It is designed to demonstrate the mathematical logic behind matrix reduction without relying on high-level libraries like NumPy for the core algorithm.

## 🛠 Features
* **Zero-Pivot Handling:** Implements logic to handle systems with potential division-by-zero errors.
* **System Diagnostics:** Identifies if a system is:
    * **Independent:** A single unique solution $(x, y, z)$.
    * **Dependent:** Infinite solutions (Linear Redundancy).
    * **Inconsistent:** No solution (Contradictory data).
* **Back Substitution:** Automatically solves for variables after reaching Row Echelon Form.

## 🚀 How to Run
Ensure you have Python 3.x installed. Run the following in your terminal:
```bash
python3 gaussian_interactive.py

# Geophysical Journal Scout: Ibadan Basement Complex

## 🌍 Research Overview
This repository contains Phase 1 of the **Project Greenland** data pipeline. The script automates the discovery of academic literature focused on groundwater exploration within the crystalline basement rocks of **Ibadan, Oyo State, Nigeria**.

The goal is to build a robust dataset comparing **1D Vertical Electrical Sounding (VES)** with **2D Electrical Resistivity Tomography (ERT)** using both conventional software and custom Python-based machine learning models.

## 🛠️ Features
- **Automated Scraping**: Leverages the `scholarly` API to survey Google Scholar.
- **Multi-Track Categorization**: Organizes results into four specific domains:
    - `1D_Links`: Traditional VES studies.
    - `2D_Links`: Advanced tomography and fracture imaging.
    - `Tech_Links`: Machine learning and inversion theory.
    - `Localized_Links`: Specific studies within Ibadan (e.g., Akinyele, Iddo LGAs).
- **Metadata Management**: Exports Title, Author, Year, and URL directly to `.csv` for rapid bibliography building.

## 🚀 Getting Started

### Prerequisites
- Anaconda (Python 3.9+)
- VS Code or Jupyter Notebook

### Installation
```bash
pip install scholarly pandas
