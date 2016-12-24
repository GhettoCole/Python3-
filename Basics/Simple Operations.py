# PROGRAMMER: Given Lepita

# Simple Operations
a = 2 + 2  # Addition
b = 5 + 4-3  # Subtraction
c = 2 * (3+4)  # Multiplication (Parentheses determine what operation comes first)
d = 10 / 2  # Division
e = (4 + 8) / 2  # Addition first then the result is divided by 2
f = (-7 + 2) * (-4)  # Negative number operation


print(a, b, c, d, e, f)
try:
    g = 11/0
except ZeroDivisionError:
    print("Cannot be divided by zero")
