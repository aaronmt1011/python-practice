# day-con.py
# This program converts a given date format (mm/dd/yyyy) into a different 
#   format (month day, year).

def day():
    print("This program recives your date input and formats it differently!\n")
    dNum = input("Enter a date (mm/dd/yyyy): ")

    m, d, y = dNum.split("/")

    month = ["January", "February", "March", "April", "May", "June", "July", 
              "August", "September", "October", "November", "December"]

    print("\nThe converted date is: {0} {1}, {2}".format(month[int(m)-1], int(d), int(y)))
    
day()