# f2c-convert.py
# This program is a simple fahrenheit to celsius converter

def c2f():
    fahr = int(input("Please enter fahrenheit (°F) temperature: "))
    
    cel = (fahr - 32) * (5/9)
    print("  ")
    print("Here is the celsius (°C) temperature: ", cel, "°F" )

    print("  ")
    input("Press the <Enter> key to exit.")


c2f()