# c2f-convert.py
# This program is a simple celsius to fahrenheit converter

def c2f():
    cel = int(input("Please enter celsius (°C) temperature: "))
    fahr = 9/5 * cel + 32
    print("  ")
    print("Here is the fahrenheit (°F) temperature: ", fahr, "°F" )

    print("  ")
    input("Press the <Enter> key to exit.")


c2f()