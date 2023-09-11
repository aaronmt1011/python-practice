# quiz-grader-5point.py
# This program gives out a grade based off of a 5 point scale scoring system

def grader():
    print("This program gives out a grade based off of user input.")
    print("The scoring system is based off of a 5 point scoring system:")
    print(" - 5 = A\n - 4 = B\n - 3 = C\n - 2 = D\n - 1 = F\n - 0 = F\n")
    score = int(input("Please enter the quiz score? "))

    if score == 5:
        print("\nThe student earned an A!")
    elif score == 4:
        print("\nThe student earned a B.")
    elif score == 3:
        print("\nThe student earned a C.")
    elif score == 2:
        print("\nThe student earned a D.")
    elif score == 1:
        print("\nThe student earned a F.")
    elif score == 0:
        print("\nThe student earned a F.")
    else:
        print("\nYou have inputted a number larger than 5 or smaller than 0. \nPlease choose a number between 0 - 5!")


grader()