# coordinateSlope.py
# This program gives out the slope between to coordinate points.

def slopeFinder():
    print("")
    print("This program gives out the slope between 2 coordinate points.")
    print("")

    print("Please input answers to the following coordinate questions as:")
    print("x y")
    print("")
    print("Don't forget to add the blank space between the x & y answer!!")
    print("")

    x1, y1 = [int(z) for z in input("What is the first points coordinates? (x y) ").split()]
    print(x1, y1)

    x2, y2 = [int(z) for z in input("What is the second points coordinates? (x y) ").split()]
    print(x2, y2)

    s = (y2 - y1) / (x2 - x1)

    print("The slope between the first coordinate (", x1,",", y1, ") and second coordinate (", x2, ",", y2, ") is ", s)

    
slopeFinder()