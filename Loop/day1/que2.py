#sum of even number

n = int(input("enter a number a here:"))
sum_even = 0
for i in range(1,n+1):
    if i%2==0:
        sum_even+=i
print("sum of even number of this number: ",sum_even)        