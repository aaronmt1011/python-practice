# month.py
# This program gives out the month by using list indexing

def month2():
    months2 = ["January", "February", "March", "April","May", "June", "July", 
               "August", "September", "October", "November", "December"]

    print("This program gives out the full name of the month! Not just the")
    print("abbreviation! All you have to do is input the months number (1-12).\n")

    m2 = int(input("Please enter the month number (1-12): "))

    print("\n" + "The month is", months2[m2-1] + "!")

month2()