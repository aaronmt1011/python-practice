# carbo_mol_calc.py
# This program gives out the molecular weight of a carbohydrate (H, C, O)
# A carbohydrate is made up of hydrogen (H), carbon (C), & oxygen (O).
# The moleculart weight of these elements is: 
#    H - 01.0079 g/mole
#    C - 12.0107 g/mole
#    O - 15.9994 g/mole


def carboCalc():
    print("")
    print("This program gives out the molecular weight (grams per mole) of ")
    print("a carbohydrate (well the elements that make-up a carbohydrate). ")
    print("All you have to do is enter the amount of each atom present!")
    print("")
    print("")

    h = (int(input("How much hydrogen atoms are there? "))) * 1.0079
    print("- - -")
    c = (int(input("How much carbon atoms are there? "))) * 12.0107
    print("- - -")
    o = (int(input("How much oxygen atoms are there? "))) * 15.9994

    print("")
    print("")
    print("The total molecular weight of hydgrogen is ", h," g/mol")
    print("- - -")
    print("The total molecular weight of hydgrogen is ", c," g/mol")
    print("- - -")
    print("The total molecular weight of hydgrogen is ", o," g/mol")
    print("- - -")
    print("The total molecular weight of everything is ", h+c+o, "g/mole")



carboCalc()