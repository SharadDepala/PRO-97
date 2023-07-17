check = int(input("Enter the year: "))
if (check % 4 == 0 and check % 100 !=0 or check%400==0):
    print("This year is a leap year!")
else:
    print("This year is not a leap year")
