# m2k-conv.py
# This program recieves an inputted miles and converts it to kilometers (km)

def m2k():
    print("This program converts miles to kilometers.")
    miles = int(input("Please enter miles: "))

    km = round(miles * 1.609344, 2)
    print("Here is the distance in kilometers:", km)

m2k()