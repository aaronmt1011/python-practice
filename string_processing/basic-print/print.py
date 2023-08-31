# print.py
# This program prints out a file

def print():
    fName = input("Enter Filename:")
    infile = open(fName, "r")
    data = infile.read()
    print(data)

print()