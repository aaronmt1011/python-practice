# month.py
# This program gives out the months abbreviation.

def month():
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"

    print("This program gives out the month of the year!")
    print("All you have to input is the months number (1-12) \n")

    m1 = int(input("Please enter the month number (1-12): "))
    pos = (m1 - 1) * 3 
    mAbbrev = months[pos:pos+3]
    print("\n" + "The month is", mAbbrev + "!")

month()