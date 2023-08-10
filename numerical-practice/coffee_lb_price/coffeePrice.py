# coffeePrice.py
# This program will give out the price per pound of coffee without shipping
# fees and the price after shipping fees are included on.

def coffeePrice():
    print("")
    print("This program gives out the price of coffee and shipping fees (if necessary).") 
    print("All you have to do is input:")
    print(" - the price per pound of coffee")
    print(" - the amount you are buying in pounds")
    print(" - & whether you want to ship it or pick it up in store")
    print("")

    c = float(input("What is the cost (per pound) of the coffee? "))
    print("- - -")
    p = float(input("What is the amount (per pound) of coffee you are buying? "))
    print("- - -")
    print("Please answer next question with either y (yes) or n (no).")
    shipping = input("Do you want to have it shipped? y/n? ")

    totCost = c * p

    if shipping == "y":
        print("")
        shippingFees = float((0.86 * p) + 1.50)
        print("")
        print("Here is the price without shipping fees: $", totCost)
        print("Here is the cost with shipping fees: $", totCost + shippingFees)
    elif shipping == "n":
        print("")
        print("Here is the price for your coffee: $", totCost)
    else:
        print("")
        print("If you got here, you did not follow the instructions.")
        print("Please follow instructions next time.")
        print("Here is the price for your coffee: $", totCost)

coffeePrice()