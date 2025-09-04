#  Age group catorization
# classify a person's age group 

age = int(input("Enter your age:"))

if age<13:
    print("person is child")
elif age>13 and age<20:
    print("person is teenager")
elif age>20 and age<60:
    print("persond is adult")
else:
    print("person is senior")




