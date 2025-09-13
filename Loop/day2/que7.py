# validate number

while True:
    number = int(input("enter the number between 1 to 10:"))
    if 1<=number<=10:
        print("Thank you!")
        break
    else:
        print("Invalid number , Try again!")