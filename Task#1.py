#Leap Year Checker:
#Create a program that determines whether a given year is a leap year
print("####Leap Year Checker####")
year = int(input("Please enter the year: "))
if year%400 == 0 and year%100 == 0:
    print("The given year is a leap year")
elif year%4 == 0 and year%100 != 0:
    print("The given year is a leap year")
else:
    print("The given year is a not a leap year")
