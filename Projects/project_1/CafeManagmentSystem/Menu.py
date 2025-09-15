menu={
    'Muglai chicken':319,
    'Chicken korma':149,
    'Chicken fry':149,
    'Chicken Biryani':129,
    'Salad':99,
    'Diet coke':49
}
print("Welcome to LAZIZ-E-JAHAN ")
print("Muglai chicken: Rs319\nChicken korma: Rs149\nChicken fry: Rs149\nChicken Biryani: Rs129\nSalad: Rs99\nDiet coke: Rs49")

Order_total = 0

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    Order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available yet!")

another_ordered= input("Do you want addanother item ? (Yes/No):")
if another_ordered == "Yes":
    item_2 = input("Enter the name of second ordered = ")
    if item_2 in menu:
        Order_total += menu[item_2]
        print(f"Your item {item_2} has been added to your order")
    else:
        print(f"Ordered item {item_2} is not available!")

print(f"The total amount if item to pay is : {Order_total}")