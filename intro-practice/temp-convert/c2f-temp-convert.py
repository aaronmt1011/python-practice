# temp-convert.py
# A simple program to convert celsius to fahrenheit 

def main():
    celsius = eval(input("Please enter °C (celsius) temperature: "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is: ", fahrenheit, "°F")

main()