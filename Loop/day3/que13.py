#print prime number

lower = int(input("enter lower number here:"))
upper = int(input("enter upper number here:"))

for number in range(lower,upper+1):
    if number>1:
        for i in range(2,number):
            if number%i==0:
                break
        else:
            print(number)
