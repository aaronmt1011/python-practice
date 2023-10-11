# reader.py
# This program reads a file and does cool things to it

# count() recieves fileHand (text file) and gives out the line count
def count(fileHand):
    count = 0
    for line in fileHand:
        count = count + 1

    print("\nTotal line Count: " , count)



# sectionread() displays only a portion of the files text
def sectionread(file, x, y):
    print(file[x:y])



# startswith() searches for lines that start with "From: " and displays them
def startswith(fileHand):
    for line in fileHand:
        # rstrip() is used to get rid of white space (\n) from text file
        line = line.rstrip()
        if line.startswith('From:') :
            print(line)



# read() is the main program body
# functions from above will be ran through read()
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

    # count(fileHand)
    # startswith(fileHand)
    file = fileHand.read()

    sectionread(file, 0, 20)

read()