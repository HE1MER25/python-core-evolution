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