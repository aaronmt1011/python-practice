# factorial.py
# This program receives an inputted number and outputs a factorial
# Factorials is the product of all positive integers less than or equal to n
# Here is the formula: 
#   n! = n * (n - 1) * ... * 1
#
# Here is a basic example:
#   5! --- 5 * (5 - 1) * (4 - 1) * (3 - 1) * (2 - 1) * 1  = 120


def factorial():
    print("")
    print("This program is a factorial program.")
    print("It will give out a factorial for any inputted number.")
    print("")
    
    num = int(input("Please enter number here: "))
    fact = 1
    for factor in range(num,1,-1):
        fact = fact * factor
    
    print("")
    print("Here is the factorial of", num, "-", fact)

factorial()