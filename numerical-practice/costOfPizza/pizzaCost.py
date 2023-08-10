# pizzaCost.py
# This program computes the cost per square inch of a pizza.

import math

def pizzaCost():
    print("")
    print("This program gives out the cost per square inch of a pizza!")
    print("Use this program when you think you may be overcharged by ")
    print("a pizza company!")
    print("")
    print("All you need to do is to enter some necessary data.")
    d = int(input("What is the diameter of the pizza in inches? - "))
    p = float(input("What is the price of the pizza? - $"))
    print("- - - - - - -")
    print("")

    a = round((math.pi * ((d/2)**2)), 2) 
    c = round((p / a), 2)

    # The following var will be used to compare costs to see if price paid
    # for the pizza costed way too much
    ulc = 0.05 # Ultra low cost
    lc = 0.08 # low cost
    mc = 0.11 # mid cost
    hc = 0.14 # high cost

    if c <= ulc:
        print("The cost of each square inch of pizza is $", c)
        print("You got an amazing deal!!! Send me the link to the pizza place please.")
    elif c <= lc:
        print("The cost of each square inch of pizza is $", c)
        print("You got a good deal!!!")
    elif c <= mc:
        print("The cost of each square inch of pizza is $", c)
        print("You got a decent deal!")
    elif c <= hc:
        print("The cost of each square inch of pizza is $", c)
        print("You got an average deal.")
    else:
        print("The cost of each square inch of pizza is $", c)
        print("Damn, you paid way too much for pizza. Look for a new pizza shop!")

pizzaCost()