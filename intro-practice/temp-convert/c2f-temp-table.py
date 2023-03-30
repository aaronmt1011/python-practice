# c2f-temp-table.py
# This program builds a "home-made" table that lays out celsius to fahrenheit temperature matchups
# then displays results in a table.


def c2f_table():
    print("Hello, this program is a celsius to fahrenheit converter.")
    print("This program will use an inputted number to fill a table with celsius to")
    print("celsius to fahrenheit conversions centered around 10 degree units (0°C, 10°C, 20°C, etc.).")
    print("   ")

    d = int(input("Please enter desired table length: ")) - 1
    print("------------------------------------")
    print("  ")
    print("  ")
    print("-------------------------")
    print("Celsius        Fahrenheit")
    print("-------        ----------")


    cel = 0
    preFahr = 32


    print(cel, "°C          ", preFahr, "°F")
    for i in range(d):
        cel = cel + 10
        fahr = (9/5 * cel) + 32
        print(cel, "°C         ", fahr, "°F")

    print("-------------------------")
    print("  ")
    print("  ")
    input("Press the <Enter> key to exit.")
    

c2f_table()