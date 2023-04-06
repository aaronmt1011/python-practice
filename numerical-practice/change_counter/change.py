# change.py
# This program takes an inputted amount of change and returns the exact
# cash amount.

def changeCounter():
    print("Change Counter!")
    print("Count your change without the hassle of counting your change!")
    print("  ")
    print("Please enter the amount for each coin:")
    print("  ")
    fullDol = int(input(" - $1 Coins: "))
    print("  ")
    halfDol = int(input(" - Half Dollars: "))
    print("  ")
    quarter = int(input(" - Quarters: "))
    print("  ")
    dime = int(input(" - Dimes: "))
    print("  ")
    nickel = int(input(" - Nickels: "))
    print("  ")
    penny = int(input(" - Pennies: "))
    print("  ")
    print("----------------")

    total = fullDol + (halfDol * .5) + (quarter * .25) + (dime * .1) + (nickel * .05) + (penny * .01)
    
    print("  ")
    print("The total cash value for the change is: ", total)
    print("  ")
    print("----------------")
    print("  ")
    input("Press <Enter> to exit.")




changeCounter()