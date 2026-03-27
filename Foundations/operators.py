# Arithmetic operators
a = 10
b = 5
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a % b)  # Modulus
print(a ** b)  # Exponentiation
print(a // b)  # Floor division
print()

#Assignment operators
x = 10
x += 5  # Equivalent to x = x + 5
print(x)
x -= 3  # Equivalent to x = x - 3
print(x)
x *= 2  # Equivalent to x = x * 2
print(x)
x /= 4  # Equivalent to x = x / 4
print(x)
x %= 3  # Equivalent to x = x % 3
print(x)
x **= 2  # Equivalent to x = x ** 2
print(x)
x //= 2  # Equivalent to x = x // 2
print(x)
print()

# Walrus operator
if (n := len("Hello")) > 5:
    print(f"Length is greater than 5: {n}" + "\n")
else:    print(f"Length is 5 or less: {n}" + "\n")

num = [1, 2, 3, 4, 5]
if (total := sum(num)) > 10:
    print(f"Total is greater than 10: {total}")
else:
    print(f"Total is 10 or less: {total}")
print()

# Comparison operators
a = 10
b = 20

print(a > b)
print(a < b)
print(a == b)
print(a <= b)
print(a >= b)
print(a != b)
