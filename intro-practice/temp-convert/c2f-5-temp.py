# c2f-temp-convert.py
# A simple program to convert celsius to fahrenheit 

def c2f():
    print("Hello, this program is a celsius to fahrenheit converter.")
    print("This program will convert 5 given temperatures.")
    print("----------------")

    for i in range(5):
        print("----------------")
        cel = int(input("Please enter °C (celsius) temperature: "))
        fahr = 9/5 * cel + 32
        print("The temperature is: ", fahr, "°F")
        print("----------------")

    print("----------------")
    input("Press the <Enter> key to exit.")

c2f()