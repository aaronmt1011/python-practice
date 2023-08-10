# lightningDistCalc.py
# This program finds how far the user is from the lighting strike based
# off of the time that has elapsed between the flash and sound of thunder.
# Speed of sound = 1100ft/sec
# 1 mile = 5280

def lightningCalc():
    print("")
    print("This program will help you find out how close you were to not ")
    print("dying from a lightning strike! All you have to do is input ")
    print("the amount of seconds between the flash and the sound of thunder.")
    print("")

    s = float(input("How much seconds passed between the flash and the sound of the thunger? "))
    d = 1100 * s
    m = round((d / 5280), 2)

    print("")
    print("You were", m, "miles away or", d, "feet away from your death due to lightning strike!")
    print("Keep watch on the skies!")

lightningCalc()