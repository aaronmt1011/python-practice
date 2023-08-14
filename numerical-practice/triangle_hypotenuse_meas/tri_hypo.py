# tri_hypo.py
# This program gives out the hypotenus of a triangle when given just an angle
# and 1 side length

import math

def tri_hypo():
    print("")
    print("This program gives out the hypotenuse of a triangle when given ")
    print("the angle and a side length.")
    print("")

    a = float(input("What is the angle of the triangle? "))
    print("")
    l = float(input("What is the side length? "))
    print("")

    h = round(l / (math.sin((math.pi / 180) * a)), 2)
    print("Here is the size of the hypotenuse ", h)


tri_hypo()