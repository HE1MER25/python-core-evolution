"""
╔══════════════════════════════════════════════════════════════════╗
║         GAUSSIAN ELIMINATION ENGINE — PYTHON IMPLEMENTATION      ║
║         HE1MER Learning Lab | Professor Ajulo-Omojesu            ║
║         All EROs Present: Interchange | Scaling | Addition       ║
╚══════════════════════════════════════════════════════════════════╝
"""

import copy

EPSILON = 1e-10  # Tolerance for floating-point zero comparison


# ─────────────────────────────────────────────
# UTILITY: PRINT MATRIX
# ─────────────────────────────────────────────
def print_matrix(matrix, label=""):
    if label:
        print(f"\n  [{label}]")
    for row in matrix:
        formatted = "  [ " + "   ".join(f"{val:8.4f}" for val in row) + " ]"
        print(formatted)


# ─────────────────────────────────────────────
# ERO 1 — INTERCHANGE: Ri ↔ Rj
# ─────────────────────────────────────────────
def ero_interchange(matrix, i, j):
    """Swap row i and row j."""
    print(f"\n  ⟶ ERO 1 | INTERCHANGE: R{i+1} ↔ R{j+1}")
    matrix[i], matrix[j] = matrix[j], matrix[i]
    return matrix


# ─────────────────────────────────────────────
# ERO 2 — SCALING: k·Ri → Ri
# ─────────────────────────────────────────────
def ero_scale(matrix, i, k):
    """Multiply row i by scalar k."""
    print(f"\n  ⟶ ERO 2 | SCALING: ({k:.4f}) × R{i+1} → R{i+1}")
    matrix[i] = [k * val for val in matrix[i]]
    return matrix


# ─────────────────────────────────────────────
# ERO 3 — ROW ADDITION: k·Ri + Rj → Rj
# ─────────────────────────────────────────────
def ero_add(matrix, i, j, k):
    """Add k times row i to row j."""
    print(f"\n  ⟶ ERO 3 | ADDITION: ({k:.4f}) × R{i+1} + R{j+1} → R{j+1}")
    matrix[j] = [k * matrix[i][col] + matrix[j][col] for col in range(len(matrix[j]))]
    return matrix


# ─────────────────────────────────────────────
# PHASE A — FORWARD ELIMINATION
# ─────────────────────────────────────────────
def forward_elimination(matrix):
    """
    Drive the matrix to Row Echelon Form (REF).
    Creates a lower triangle of zeros using EROs 1, 2, and 3.
    """
    n = len(matrix)
    print("\n" + "═"*60)
    print("  PHASE A — FORWARD ELIMINATION")
    print("═"*60)

    for col in range(n):
        print(f"\n  ── Pivot Column: {col+1} ──")

        # Find pivot row (partial pivoting — ERO 1 readiness)
        max_row = col
        for row in range(col + 1, n):
            if abs(matrix[row][col]) > abs(matrix[max_row][col]):
                max_row = row

        # ERO 1: Interchange if needed
        if max_row != col:
            matrix = ero_interchange(matrix, col, max_row)
            print_matrix(matrix, "After Interchange")

        # Check if pivot is effectively zero (singular column)
        if abs(matrix[col][col]) < EPSILON:
            print(f"\n  ⚠ Zero pivot at column {col+1}. Skipping scaling.")
            continue

        # ERO 2: Scale to get a leading 1
        pivot = matrix[col][col]
        if abs(pivot - 1.0) > EPSILON:
            matrix = ero_scale(matrix, col, 1.0 / pivot)
            print_matrix(matrix, "After Scaling")

        # ERO 3: Eliminate all values below the pivot
        for row in range(col + 1, n):
            if abs(matrix[row][col]) > EPSILON:
                factor = -matrix[row][col]
                matrix = ero_add(matrix, col, row, factor)
                print_matrix(matrix, f"After Eliminating R{row+1}, Col {col+1}")

    return matrix


# ─────────────────────────────────────────────
# PHASE B — BACKWARD SUBSTITUTION
# ─────────────────────────────────────────────
def backward_substitution(matrix):
    """
    Extract solutions from Row Echelon Form.
    Propagates values upward from the bottom row.
    """
    n = len(matrix)
    solution = [0.0] * n

    print("\n" + "═"*60)
    print("  PHASE B — BACKWARD SUBSTITUTION")
    print("═"*60)

    for row in range(n - 1, -1, -1):
        # RHS value
        rhs = matrix[row][n]

        # Subtract known variables
        for col in range(row + 1, n):
            rhs -= matrix[row][col] * solution[col]

        pivot = matrix[row][row]
        if abs(pivot) > EPSILON:
            solution[row] = rhs / pivot
            print(f"\n  Variable x{row+1} = {solution[row]:.4f}")

    return solution


# ─────────────────────────────────────────────
# DIAGNOSTIC ENGINE — OUTCOME INTERPRETATION
# ─────────────────────────────────────────────
def interpret_outcome(matrix):
    """
    Reads the final REF matrix and classifies the system:

    ┌─────────────────────────────────────────────────────┐
    │ INCONSISTENT     → 0 = non-zero  → No solution      │
    │ CONSISTENT & DEP → 0 = 0         → Infinite solutions│
    │ CONSISTENT & IND → Unique pivot  → One solution     │
    └─────────────────────────────────────────────────────┘
    """
    n = len(matrix)
    zero_rows = 0

    print("\n" + "═"*60)
    print("  DIAGNOSTIC: SYSTEM CLASSIFICATION")
    print("═"*60)

    for row in matrix:
        coeffs = row[:-1]
        rhs    = row[-1]

        all_zero_coeffs = all(abs(c) < EPSILON for c in coeffs)

        if all_zero_coeffs:
            if abs(rhs) > EPSILON:
                # ── INCONSISTENT ──
                print("""
  ┌─────────────────────────────────────────┐
  │  OUTCOME: INCONSISTENT SYSTEM           │
  │  Row reads: 0 = {:.4f}                 │
  │  This is a mathematical contradiction.  │
  │  → No solution exists.                  │
  │  In geophysics: sensor conflict or      │
  │    corrupted field data detected.       │
  └─────────────────────────────────────────┘
                """.format(rhs))
                return "inconsistent"
            else:
                # ── CONSISTENT & DEPENDENT ──
                zero_rows += 1

    if zero_rows > 0:
        print("""
  ┌──────────────────────────────────────────────┐
  │  OUTCOME: CONSISTENT & DEPENDENT             │
  │  Row reads: 0 = 0 (redundant equation)       │
  │  → Infinitely many solutions exist.          │
  │  System has a free variable.                 │
  │  In geophysics: insufficient field           │
  │    measurements — underdetermined model.     │
  └──────────────────────────────────────────────┘
        """)
        return "dependent"

    # ── CONSISTENT & INDEPENDENT ──
    print("""
  ┌──────────────────────────────────────────────┐
  │  OUTCOME: CONSISTENT & INDEPENDENT          │
  │  Unique pivot in every row.                  │
  │  → One unique solution exists.               │
  │  System is fully determined.                 │
  │  In geophysics: clean delineation result —  │
  │    subsurface model resolved precisely.      │
  └──────────────────────────────────────────────┘
    """)
    return "independent"


# ─────────────────────────────────────────────
# MAIN GAUSSIAN ENGINE
# ─────────────────────────────────────────────
def gaussian_elimination(augmented_matrix):
    """
    Master function. Runs full Gaussian Elimination pipeline:
    Forward Elimination → Classification → Backward Substitution
    """
    matrix = copy.deepcopy(augmented_matrix)
    n = len(matrix)

    print("\n" + "█"*60)
    print("  GAUSSIAN ELIMINATION ENGINE — HE1MER LEARNING LAB")
    print("█"*60)

    print_matrix(matrix, "INITIAL AUGMENTED MATRIX")

    # Phase A
    matrix = forward_elimination(matrix)

    print("\n" + "─"*60)
    print_matrix(matrix, "FINAL ROW ECHELON FORM (REF)")

    # Diagnostic
    outcome = interpret_outcome(matrix)

    # Phase B — only if unique solution possible
    if outcome == "independent":
        solution = backward_substitution(matrix)

        print("\n" + "█"*60)
        print("  FINAL SOLUTION")
        print("█"*60)
        for i, val in enumerate(solution):
            print(f"  x{i+1} = {val:.4f}")
        print()
        return solution

    return None


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":

    print("\n" + "▓"*60)
    print("  TEST 1: CONSISTENT & INDEPENDENT (Unique Solution)")
    print("  System: x + y + z = 6 | 2x+3y+z=14 | x+2y+3z=14")
    print("▓"*60)
    A1 = [
        [1, 1, 1, 6],
        [2, 3, 1, 14],
        [1, 2, 3, 14]
    ]
    gaussian_elimination(A1)

    print("\n\n" + "▓"*60)
    print("  TEST 2: INCONSISTENT (No Solution)")
    print("  System: x+y=3 | x+y=5")
    print("▓"*60)
    A2 = [
        [1, 1, 3],
        [1, 1, 5]
    ]
    gaussian_elimination(A2)

    print("\n\n" + "▓"*60)
    print("  TEST 3: CONSISTENT & DEPENDENT (Infinite Solutions)")
    print("  System: x+y=4 | 2x+2y=8")
    print("▓"*60)
    A3 = [
        [1, 1, 4],
        [2, 2, 8]
    ]
    gaussian_elimination(A3)
