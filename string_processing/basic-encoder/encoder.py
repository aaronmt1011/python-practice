# encoder.py
# This program turns text into a series of unicode codes for each character
# Simply put, this program gives out a secret code from inputted text

def encoder():
    print("This program turns your text into a secret code!\n")
    
    mes = input("What text do want to be turned into a code? \n")
    
    for ch in mes:
        print(ord(ch), end = " ")

    print()

encoder()
