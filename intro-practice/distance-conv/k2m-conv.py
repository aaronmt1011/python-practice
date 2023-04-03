# k2m-conv.py
# This program recieves an inputted kilometers (km) and converts it to miles

def k2m():
    km = int(input("Enter kilometers:"))
    miles = round(km * 0.621371, 2)
    print(miles)

k2m()