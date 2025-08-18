print("calculate how many seconds in a year")
print()
secondsInAMin = int(input("how many seconds make one minute?: "))
minutesInAHour = int(input("how many minutes make an hour?: "))
hoursInADay = int(input("how many hours make a day?: "))
leapYear = input("is it a leap year?: ")
if leapYear == "yes" or leapYear == "Yes":
    daysInAYear = 366
    secondsInAYear = secondsInAMin * minutesInAHour * hoursInADay * daysInAYear
    print("we have", secondsInAYear, "seconds in a leap year") 
else: 
    leapYear == "no" or leapYear == "No"
    daysInAYear = 365
    secondsInAYear = secondsInAMin * minutesInAHour * hoursInADay * daysInAYear
    print("we have", secondsInAYear, "seconds in a normal year")
    

        

