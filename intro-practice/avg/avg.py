# avg.py
# This program gives the average of the 2 input numbers

def main():
    print("This program computes the average of 2 numbers")

    num1, num2 = eval(input("Enter two numbers separated by a comma: "))
    average = (num1 + num2) / 2
    print("The average of the 2 numbers is: ", average)

main()