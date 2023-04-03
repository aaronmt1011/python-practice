# k2m-conv.py
# This program recieves an inputted kilometers (km) and converts it to miles

def k2m():
    print("This program converts kilometers to miles.")
    km = int(input("Please enter kilometers: "))

    miles = round(km * 0.621371, 2)
    print("Here is the distance in miles:", miles)

k2m()