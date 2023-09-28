# reader.py
# This program reads a file and does cool things to it

def read():
    print("This program reads a file and does cool stuff with it. There is \nalso a default text file that is included within the project folder \nthat can be used. You can also input your own text file. Just \nmake sure to place own file in the same location as the reader.py.\n")
    print("Please answer the following question with a 'y' or 'n'.")
    answer = input("Do you want to use the given text file? ")
    while answer != "n" and answer != "y":
        print("\nPlease enter either 'y' or 'n' answer")
        answer = input("Do you want to use the given text file? ")
    
    if answer == "y":
        fileHand = open('repos/python-practice/reading_files/text-reader/mbox.txt')
    
    
    elif answer == "n":
        print("\nMake sure to have file path for own text file for the next question. \nFor example the location of the default text file was: \nrepos/python-practice/reading_files/text-reader/mbox.txt")
        while True:
            try:
                fileHand = open(input("\nPlease input the files path: "))
                break
            except FileNotFoundError:
                print("\nPlease input the files path CORRECTLY next time.")

    # The following code is the easiest way to read through an entire ext file
    for lines in fileHand:
        print(lines)


read()