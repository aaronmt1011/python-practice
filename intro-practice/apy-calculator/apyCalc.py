# apyCalc.py
# This program uses numerous inputs and returns the value of an investment after 
# an inputted amount of years.

# Use below to help with understanding some of the financial aspects: 
# apy is short for annual percentage yield
# apy is used to calculate interest rates earned on an investment/deposit while 
# also adding on the effects of compound interest 

# nominal interest rate is the initial rate that is provided before compound interest.

# compounding periods are based off of daily, monthly, quarterly, semi-annually, or annually

def investment():
    print("This program calculates an investment based off of an inputted amount of years.")
    
    cash = int(input("Enter the initial amount: "))
    year = int(input("Enter the amount of years for the investment: "))
    rate = int(input("Enter the nominal interest rate: "))
    freq = int(input("Enter the compounding periods for the year: "))

    apy = ((1 + ((rate/100) / freq)) ** freq) - 1 
    apyPerc = apy * 100
    apyRound = round(apyPerc, 2)
    initCash = cash

    for i in range(year):
        cash = cash * (1 + apy)

    cashRound = round(cash, 2)
    totInt = round(cashRound - initCash, 2)

    print("--------")
    print("The apy value is:", apyRound, "%")
    print("The value in", year, "years will be:", cashRound)
    print("The interest gained is:", totInt)

investment()