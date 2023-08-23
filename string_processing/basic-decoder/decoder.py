# decoder.py
# This program recieves a coded message and returns the decoded text

def decoder():
    print("This program decodes your coded messages!\n")
    code = input("What is your coded message?\n")

    mes = ""

    for m in code.split():
        codeI = int(m)
        mes = mes + chr(codeI)

    print("\nThe decoded text is: \n" + mes)

decoder()