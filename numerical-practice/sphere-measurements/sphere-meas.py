# sphere-meas.py
# This program shows results for various sphere measurements
import math

def sphere():
    print("")
    print("This program provides surface area and volume measurements for a sphere.")
    print("All you have to do is provide the radius of the sphere.")
    print("")
    n = int(input("Please enter the radius of the sphere: "))

    sa = round(4 * math.pi * (n**2))
    v = round(((4/3) * math.pi * (n**3)), 2) 
    
    print("")
    print("----------------------------")
    print("")
    print("Here is the surface area of the sphere:", sa)
    print("")
    print("Here is the volume of the sphere:", v)
    print("")
    print("----------------------------")
    print("")
    input("Press <Enter> to exit program.")

sphere()