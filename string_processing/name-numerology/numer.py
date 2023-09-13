# numer.py
# This program gives out your name's total "number"

def numer():
    print("This progam gives out a name's 'number'. A name's number comes from\nconverting each letter to a number based off of alphabetical order and \nadding them together to get the total name's number (spaces are ignored).\n")
    name = input("Please enter a name here: ")
    sn = name.upper().split()
    jn = "".join(sn)
    num = 0

    for ch in jn:
        num = (ord(ch) - 64) + num

    print("\nHere is the name's 'number': " + str(num))


numer()