# tri_area.py
# This program gives out the area of a tringle

import math

def triArea():
    print("")
    print("This program gives out the area of a triangle.")
    print("All you (user) have to do is input the length of the 3 sides.")
    print("")

    print("Please input answers as: ")
    print("a b c")
    print("")
    a, b, c = [int(z) for z in input("What are the lengths of the 3 sides? ").split()]
    print("")

    s = (a + b + c) / 2
    
    area = round(math.sqrt(s * (s - a) * (s - b) * (s - c)), 4)

    print("Here is the area of the triangle: ", area)

triArea()