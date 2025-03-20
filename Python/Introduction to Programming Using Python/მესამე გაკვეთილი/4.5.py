todaysday = int(input("Enter today's day: "))
numberofdays = todaysday + int(input("Enter the number of days elapsed since today:"))
number = ""
if todaysday == 0:
    number = "Sunday"

elif todaysday == 1:
    number = "Monday"

elif todaysday == 2:
    number = "Tuesday"

elif todaysday == 3:
    number = "Wednesday"

elif todaysday == 4:
    number = "Thursday"

elif todaysday == 5:
    number = "Friday"

elif todaysday == 6:
    number = "Saturday"

#---------------------------------------
number1 = ""
if numberofdays == 0 or numberofdays == 7 or numberofdays == 14 or numberofdays == 21 or numberofdays == 28:
    number1 = "Sunday"

elif numberofdays == 1 or numberofdays == 8 or numberofdays == 15 or numberofdays == 22 or numberofdays == 29:
    number1 = "Monday"

elif numberofdays == 2 or numberofdays == 9 or numberofdays == 16 or numberofdays == 23 or numberofdays == 30:
    number1 = "Tuesday"

elif numberofdays == 3 or numberofdays == 10 or numberofdays == 17 or numberofdays == 24 or numberofdays == 31:
    number1 = "Wednesday"

elif numberofdays == 4 or numberofdays == 11 or numberofdays == 18 or numberofdays == 25:
    number1 = "Thursday"

elif numberofdays == 5 or numberofdays == 12 or numberofdays == 19 or numberofdays == 26:
    number1 = "Friday"

elif  numberofdays == 6 or numberofdays == 13 or numberofdays == 20 or numberofdays == 27:
    number1 = "Saturday"

print(f"Today is {number} and the future day is {number1}")