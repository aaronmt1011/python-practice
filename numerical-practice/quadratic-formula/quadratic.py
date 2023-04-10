# quadratic.py
# This program computes the roots for a quadratic equation.
# This program may crash if no roots are found.

import math

def quad():
    print("This program is used to solve a quadratic equation.")
    print("   ")

    a = float(input("Enter a coefficient (value): "))
    b = float(input("Enter b coefficient (value): "))
    c = float(input("Enter c coefficient (value): "))
    discRoot = math.sqrt((b * b) - (4 * a * c))
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)

    print("   ")
    print("The solutions is", root1, "and", root2)

quad()