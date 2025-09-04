"""movie ticket pricing
movie ticket are priced based on age
$12 for adults (18 or above)  
$8 for children 
every one gets discounts $2 on wednesday"""

age = int(input("enter your age:"))
day = input("enter today's day:")

price =12
if age>=18:
    print 
else:
    price = 8
print(price)

if day == "wedenesday":
    print("yayy you get $2 disount today")
    price-=2
else:
    print("you didn't get any discount ")
print(price)    

