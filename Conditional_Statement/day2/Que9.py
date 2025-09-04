#leap year checker

year = int(input("Enter that year which is used to check:"))
if year%4==0:
    print("This is leap year")
elif year%400==0:
    print("This is leap year")
else:
    print("This is not leap year")
