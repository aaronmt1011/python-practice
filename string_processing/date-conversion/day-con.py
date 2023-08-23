# day-con.py
# This program converts a given date format (mm/dd/yyyy) into a different 
#   format (month day, year).

def day():
    print("This program recives your date input and formats it differently!\n")
    dNum = input("Enter a date (mm/dd/yyyy): ")

    mm, dd, yy = dNum.split("/")

    month = ["January", "February", "March", "April", "May", "June", "July", 
              "August", "September", "October", "November", "December"]

    mm = month[int(mm)-1]

    print("\nThe converted date is:", mm, dd + ",", yy)
    
day()