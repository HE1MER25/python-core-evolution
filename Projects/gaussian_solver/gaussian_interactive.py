"""
╔══════════════════════════════════════════════════════════════════╗
║     INTERACTIVE GAUSSIAN ELIMINATION ENGINE — PYTHON             ║
║     HE1MER Learning Lab | Professor Ajulo-Omojesu                ║
║     User-Driven: 2X2 or 3X3 | Full ERO Pipeline                 ║
╚══════════════════════════════════════════════════════════════════╝
"""

import copy

EPSILON = 1e-10


# ─────────────────────────────────────────────
# UTILITY
# ─────────────────────────────────────────────
def divider(char="=", width=58):
    print("\n  " + char * width)

def print_matrix(matrix, label=""):
    if label:
        print(f"\n  [{label}]")
    for row in matrix:
        formatted = "  [ " + "   ".join(f"{v:8.4f}" for v in row) + " ]"
        print(formatted)

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  ⚠  Invalid input. Enter a number.")


# ─────────────────────────────────────────────
# EROs
# ─────────────────────────────────────────────
def ero_interchange(M, i, j):
    print(f"\n  ⟶ ERO 1 | INTERCHANGE: R{i+1} ↔ R{j+1}")
    M[i], M[j] = M[j], M[i]

def ero_scale(M, i, k):
    print(f"\n  ⟶ ERO 2 | SCALING: ({k:.4f}) × R{i+1} → R{i+1}")
    M[i] = [k * v for v in M[i]]

def ero_add(M, i, j, k):
    print(f"\n  ⟶ ERO 3 | ADDITION: ({k:.4f}) × R{i+1} + R{j+1} → R{j+1}")
    M[j] = [k * M[i][c] + M[j][c] for c in range(len(M[j]))]


# ─────────────────────────────────────────────
# PHASE A — FORWARD ELIMINATION
# ─────────────────────────────────────────────
def forward_elimination(M):
    n = len(M)
    divider("=")
    print("  PHASE A — FORWARD ELIMINATION")
    divider("=")

    for col in range(n):
        print(f"\n  ── Pivot Column: {col+1} ──")

        # Partial pivot
        max_row = max(range(col, n), key=lambda r: abs(M[r][col]))
        if max_row != col:
            ero_interchange(M, col, max_row)
            print_matrix(M, "After Interchange")

        if abs(M[col][col]) < EPSILON:
            print(f"\n  ⚠  Zero pivot at column {col+1}. Skipping.")
            continue

        # Scale to leading 1
        pivot = M[col][col]
        if abs(pivot - 1.0) > EPSILON:
            ero_scale(M, col, 1.0 / pivot)
            print_matrix(M, "After Scaling")

        # Eliminate below
        for row in range(col + 1, n):
            if abs(M[row][col]) > EPSILON:
                ero_add(M, col, row, -M[row][col])
                print_matrix(M, f"After Eliminating R{row+1}, Col {col+1}")


# ─────────────────────────────────────────────
# PHASE B — BACKWARD SUBSTITUTION
# ─────────────────────────────────────────────
def backward_substitution(M, var_names):
    n = len(M)
    sol = [0.0] * n
    divider("=")
    print("  PHASE B — BACKWARD SUBSTITUTION")
    divider("=")

    for row in range(n - 1, -1, -1):
        rhs = M[row][n]
        for col in range(row + 1, n):
            rhs -= M[row][col] * sol[col]
        pivot = M[row][row]
        if abs(pivot) > EPSILON:
            sol[row] = rhs / pivot
            print(f"\n  {var_names[row]} = {sol[row]:.4f}")
    return sol


# ─────────────────────────────────────────────
# DIAGNOSTIC
# ─────────────────────────────────────────────
def diagnose(M, n):
    divider("=")
    print("  DIAGNOSTIC: SYSTEM CLASSIFICATION")
    divider("=")

    zero_rows = 0
    for row in M:
        coeffs_zero = all(abs(row[c]) < EPSILON for c in range(n))
        if coeffs_zero:
            if abs(row[n]) > EPSILON:
                print("""
  ┌─────────────────────────────────────────────────┐
  │  OUTCOME: INCONSISTENT                          │
  │  A row reads  0 = non-zero  — contradiction.   │
  │  → No solution exists.                          │
  │  Geophysics flag: sensor conflict or bad data.  │
  └─────────────────────────────────────────────────┘""")
                return "inconsistent"
            else:
                zero_rows += 1

    if zero_rows:
        print("""
  ┌─────────────────────────────────────────────────┐
  │  OUTCOME: CONSISTENT & DEPENDENT                │
  │  A row reads  0 = 0  — redundant equation.     │
  │  → Infinitely many solutions (free variable).   │
  │  Geophysics flag: underdetermined model.        │
  └─────────────────────────────────────────────────┘""")
        return "dependent"

    print("""
  ┌─────────────────────────────────────────────────┐
  │  OUTCOME: CONSISTENT & INDEPENDENT              │
  │  Every row has a unique pivot.                  │
  │  → Exactly one solution exists.                 │
  │  Geophysics flag: model fully resolved.         │
  └─────────────────────────────────────────────────┘""")
    return "independent"


# ─────────────────────────────────────────────
# INPUT: GET MATRIX FROM USER
# ─────────────────────────────────────────────
def get_matrix(n):
    """
    Prompts user for coefficients row by row.
    n = 2 → variables: x, y
    n = 3 → variables: x, y, z
    """
    var_names = ["x", "y", "z"][:n]
    lhs_labels = var_names + ["RHS (constant)"]

    print(f"\n  Enter coefficients for each equation.")
    print(f"  Format per row: {' | '.join(lhs_labels)}\n")

    matrix = []
    for eq in range(1, n + 1):
        print(f"  ── Equation {eq} ──")
        row = []
        for var in var_names:
            val = get_float(f"    Coefficient of {var}: ")
            row.append(val)
        rhs = get_float(f"    Right-hand side (constant): ")
        row.append(rhs)
        matrix.append(row)
        print()

    return matrix, var_names


# ─────────────────────────────────────────────
# DISPLAY SYSTEM AS EQUATIONS
# ─────────────────────────────────────────────
def display_system(matrix, var_names):
    print("\n  Your system of equations:")
    for row in matrix:
        terms = [f"({row[i]:.2f}){var_names[i]}" for i in range(len(var_names))]
        eq = "  " + " + ".join(terms) + f" = {row[-1]:.2f}"
        print(eq)


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────
def main():
    print("\n" + "█" * 60)
    print("  GAUSSIAN ELIMINATION — INTERACTIVE ENGINE")
    print("  HE1MER Learning Lab | Pristine Standard")
    print("█" * 60)

    while True:
        # ── STEP 1: Choose matrix size ──
        divider("-")
        print("\n  SELECT MATRIX DIMENSION:\n")
        print("    [1]  2×2  (variables: x, y)")
        print("    [2]  3×3  (variables: x, y, z)")
        print("    [0]  Exit\n")

        choice = input("  Your choice: ").strip()

        if choice == "0":
            print("\n  Engine closed. Execute with precision.\n")
            break

        if choice == "1":
            n = 2
        elif choice == "2":
            n = 3
        else:
            print("  ⚠  Invalid choice. Enter 1, 2, or 0.")
            continue

        print(f"\n  Selected: {n}×{n} system")

        # ── STEP 2: Input coefficients ──
        matrix, var_names = get_matrix(n)
        display_system(matrix, var_names)

        # ── STEP 3: Confirm before solving ──
        confirm = input("\n  Proceed with elimination? (y/n): ").strip().lower()
        if confirm != "y":
            print("  Restarting input...\n")
            continue

        # ── STEP 4: Run elimination ──
        M = copy.deepcopy(matrix)

        divider("█")
        print("  GAUSSIAN ELIMINATION ENGINE — RUNNING")
        divider("█")

        print_matrix(M, "INITIAL AUGMENTED MATRIX")
        forward_elimination(M)

        divider("-")
        print_matrix(M, "FINAL ROW ECHELON FORM (REF)")

        outcome = diagnose(M, n)

        if outcome == "independent":
            sol = backward_substitution(M, var_names)

            divider("█")
            print("  FINAL SOLUTION")
            divider("█")
            for name, val in zip(var_names, sol):
                print(f"  {name} = {val:.4f}")

            # Verification
            print("\n  VERIFICATION:")
            for i, row in enumerate(matrix):
                computed = sum(row[j] * sol[j] for j in range(n))
                status = "✓" if abs(computed - row[n]) < 1e-6 else "✗"
                print(f"  Equation {i+1}: {computed:.4f} = {row[n]:.4f}  {status}")

        # ── Repeat? ──
        again = input("\n  Solve another system? (y/n): ").strip().lower()
        if again != "y":
            print("\n  Engine closed. Execute with precision.\n")
            break


if __name__ == "__main__":
    main()
