# change-counter.py
# This program gives out the value of inputted change. The program should be 
# more accurate due to the usage of ints rather than float.


def change_pt2():
    print("This program is a change counter! All you have to do is input the")
    print("amount of change (of each type) into the program.")
    print("Please enter the amount for each coin:\n")

    fullDol = int(input(" - $1 Coins: ")) * 100
    halfDol = int(input(" - Half Dollars: ")) * 50
    quarter = int(input(" - Quarters: ")) * 25
    dime = int(input(" - Dimes: ")) * 10
    nickel = int(input(" - Nickels: ")) * 5
    penny = int(input(" - Pennies: "))
    print("\n----------------------------------------\n")

    total = fullDol + halfDol + quarter + dime + nickel + penny

    print("The total value of your change is ${0}.{1:0>2}"
          .format(total//100, total%100))
    
    print("\n----------------------------------------")


change_pt2()