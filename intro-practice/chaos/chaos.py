# File: chaos.py
# Simple program that shows "chaotic" numbers
# Please refrain from putting numbers larger than 1. The number will get tooooo big

def main():
    print("This program shows a basic chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 3.9 * x * (1 - x)
        print(x)

main()