#WAP to chehck if a number is single digit number , 2 digit number and 
# so on ,,,, up to 5 digits

num = int(input("enter a number here upto 5 digits:"))
if num>=0 and num<=9:
    print("it is single digit number")
elif num>=10 and num<=99:
    print("it is double digit number")
elif num>=100 and num<=999:
    print("it is three digit number")
elif num>=1000 and num<=9999:
    print("it is four digit number")
elif num>=10000 and num<=99999:
    print("it is five digit number")
else:
    print("number more than five digit ")
