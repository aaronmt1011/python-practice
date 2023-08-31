# usernames.py
# This program creates a file of usernames from a file of names (First & Last name only)

def uname():
    print("This program creates a file of usernames by using an input file.")
    print("The input file should have names inside of it.\n")

    iniName = input("Please enter the input names file here: ")
    outiName = input("\nPlease enter the output file to place created usernames into:")

    ini = open(iniName, "r")
    outi = open(outiName, "w")

    # for loop goes through each line of ini (input file), creates a usersname
    # from the name, and then places usernames into outi (output file).
    for line in ini:
        first, last = line.split()
        uname = (first[0] + last[:7]).lower()
        print(uname, file=outi)

    ini.close()
    outi.close()

    print("Usernames have been places into", outiName)

uname()