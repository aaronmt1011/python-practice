# tenYearInv.py
# This program uses 2 inputs (initial amount & apy) and
# returns the value of an investment 10 years into the future.

# Use below to help with understanding the financial aspects: 
# apy is short for annual percentage yield
# apy is used to calculate interest rates earned on an investment/deposit while 
# also adding on the effects of compound interest 

# compounding periods are based off of daily, monthly, quarterly, semi-annually, or annually

def investment():
    print("This program calculates a ten year investment for your stash!")
    
    rate = eval(input("Enter the nominal interest rate: "))
    freq = eval(input("Enter the compounding periods for the year: "))
    cash = eval(input("Enter the initial amount: "))

    apy = ((1 + ((rate/100) / freq)) ** freq) - 1 
    apyPerc = apy * 100
    apyRound = round(apyPerc, 2)

    for i in range(10):
        cash = cash * (1 + apy)

    cashRound = round(cash, 2)

    print("--------")
    print("The apy value is: ", apyRound, "%")
    print("The value in 10 years is: ", cashRound)

investment()