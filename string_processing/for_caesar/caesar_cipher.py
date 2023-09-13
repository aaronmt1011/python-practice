# caesar_cipher.py
# This program is based off of caesar cipher (details are in README.md)

def c_encoder():
    print("This is the first part of the caesar cipher program, the encoding part. \nThe encoder works by shifting each letter to a different position to \nmake message unreadable.")
    code = input("Please enter the message you want to be encoded: ")
    position = input("Please enter the shift direction using pos or neg: ")
    key = int(input("Please enter the number that you would like each letter to be shifted by: "))

    alphabet = "abcdefghijklmnopqrstuv"
    secretCode = ""

    sc = code.upper().split()
    num = 0

    for x in sc:
        for ch in x:
            if position == "pos":
                num = (ord(ch) - 65) + key
                if num > 25:
                    print(num - 26)
                    #print(alphabet[num - 26])
                
                else:
                    print(num)
                    #print(alphabet[num])

            elif position == "neg":
                num = (ord(ch) - 65) - key
                if num < 0:
                    print(num + 26)
                    #print(alphabet[num + 26])
                
                else:
                    print(num)
                    #print(alphabet[num])
            
            else:
                num = (ord(ch) - 65) + key
                if num > 25:
                    print(num - 26)
                    #print(alphabet[num - 26])
                
                else:
                    print(num)
                    #print(alphabet[num])


c_encoder()




# def c_decoder():


# c_decoder()