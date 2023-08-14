# coordinate_dist.py
# This program gives out the distance between 2 coordinate points

import math

def distFinder():
    print("")
    print("This program gives out the distance between 2 coordinate points.")
    print("")

    print("Please input answers to the following coordinate questions as:")
    print("x y")
    print("")
    print("Don't forget to add the blank space between the x & y answer!!")
    print("")

    x1, y1 = [int(z) for z in input("What is the first points coordinates? (x y) ").split()]
    print("")
    x2, y2 = [int(z) for z in input("What is the second points coordinates? (x y) ").split()]

    d = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))

    print("")
    print("This is the distance between the 2 coordinates: ", d)


distFinder()