# acro.py
# This program gives out an acronym

def acro():
    print("This program creates an acronym out of your inputted words!\n")
    w = input("Please enter words here: ")
    sw = w.split()

    acro = ""
    for x in sw:
        acro = acro + x[0]

    print("\nHere is your acronym: " + acro.upper())

acro()