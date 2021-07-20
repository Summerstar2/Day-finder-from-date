import random
import time
import datetime
def Do_again():
    Use=str(input("Do you want to use the program again? (Yes/No) "))
    if Use=="No":
        return False
    return True
def Enter_dateagain():
    Newdate=str(input("Do you wish to enter a new date? (Yes/No) "))
    if Newdate=="No":
        return False
    return True
Weekdays=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
print ("Welcome to the day calculator, enter a date manually or have the system generate one for you.")
Date=str(input("Do you want to enter a date manually? (Yes/No) - "))
while True:
    if Date=="No":
        print ("The system will generate a date for you.")
        Day=random.randint(1,31)
        Month=random.randint(1,12)
        Year=random.randint(1000,9999)
        time.sleep(0.5)
        print (".")
        time.sleep(0.5)
        print ("..")
        time.sleep(0.5)
        print ("...")
        time.sleep(0.8)
        print (Day,"/", Month,"/", Year)
        Weeknumber=datetime.date(Year,Month,Day).weekday()
        print ("The day on this date is ",Weekdays[Weeknumber])
    if Date=="Yes":
            while True:
                Day=int(input("Enter day - "))
                while Day>31:
                    print ("Invalid day, try again.")
                    Day=int(input("Enter day - "))
                else:
                    Month=int(input("Enter month - "))
                    while Month>12:
                        print ("Invalid month, try again.")
                        Month=int(input("Enter month - "))
                    else:
                        Year=int(input("Enter any year - "))
                        while Year<1000 or Year>9999:
                            print ("Number of digits shouldn't exceed or be less than 4. Try again.")
                            Year=int(input("Enter year - "))
                        print ("The date you entered is - ",Day,"/", Month,"/", Year) 
                        Weeknumber=datetime.date(Year,Month,Day).weekday()
                        print ("The day on this date is",Weekdays[Weeknumber])
                if not Enter_dateagain():
                    break
    if not Do_again():
        break