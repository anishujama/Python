#wap to create billing system at supermarket
while True:
    Name = input("enter customer's name:")
    total = 0

    while True:
        print("enter the amount and quantity")
        amount = float(input("enter amount:"))
        quantity = float(input("enter quantity:"))
        total += amount*quantity
        repeat = input("do you want to add more items? (yes/no): ")
        if repeat == "no" or repeat == "No":
            break
    print("-"*40)
    print("Name:",Name)  
    print("Amount to be paid:",total)
    print("-"*40)
    print("***********Happy shoping*********")

    repeat1 = input("do you want to go to the next customer? (yes/no):")
    if repeat1=="no" or repeat1=="No":
        break

