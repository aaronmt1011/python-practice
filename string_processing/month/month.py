# month.py
# This program gives out the month.

def month():
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"

    print("This program gives out the month of the year!")
    print("All you have to input is the months number (1-12) \n")

    n = int(input("Please enter the month number (1-12): "))
    pos = (n -1) * 3 
    month = months[pos:pos+3]
    print("\n" + "The month is", month + "!")

month()