# avg.py
# This program gives the average of the 2 input numbers

def main():
    print("This program computes the average of 3 numbers")

    num1, num2, num3 = eval(input("Enter three numbers separated by a comma: "))
    average = (num1 + num2 + num3) / 3
    print("The average of the 3 numbers is: ", average)

main()