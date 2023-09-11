# grader-per.py
# This program gives out a grade based off of an inputted percantage

def grader_pt2():
    print("This program gives out a grade based off of user input.")
    print("The scoring system is based off of a percentage system:\n")
    print(' - A: 90{0} - 100{0}\n - B: 80{0} - 89{0}\n - C: 70{0} - 79{0}\n - D: 60{0} - 69{0}\n - F: 0{0} - 59{0}\n'.format("%"))
    perc = float(input("Please enter the quiz percentage score: "))
    p = round(perc, 2)

    if p >= 90 and p <= 100:
        print("\nThe student earned an A!")
    elif p >= 80 and p < 90:
        print("\nThe student earned a B.")
    elif p >= 70 and p < 80:
        print("\nThe student earned a C.")
    elif p >= 60 and p < 70:
        print("\nThe student earned a D.")
    elif p >= 0 and p < 60:
        print("\nThe student earned a F.")
    else:
        print("\nYou have inputted a number larger than 100 or smaller than 0. \nPlease choose a number between 0 - 100!")




grader_pt2()