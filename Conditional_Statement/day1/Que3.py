'''grade calculator
Assign a letter grade based on student score'''

score = int(input("Enter marks of student:"))
if score>=90 and score<=100:
    print("Student gets A grade in exam ")
elif score>=80 and score<=89:
    print("Student gets B grade in exam ")
elif score>=70 and score<=79:
    print("Student gets C grade in exam ")
elif score>=60 and score<=69:
    print("Student gets D grade in exam ")
elif score<60:
    print("Student gets F grade in exam ")
else:
    print("invalid marks")