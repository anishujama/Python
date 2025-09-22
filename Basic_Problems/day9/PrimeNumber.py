#wap to check if a number is prime or not

n = int(input("enter a number here:"))
if n<=1:
    print("It is not a prime number")
else:
    for i  in range(2,n):
        if n%i==0:
            print("it is not a prime number")
            break
    else:
         print("it is prime number" )