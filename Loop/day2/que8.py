#check number is prime or not

number = int(input("enter a number here :"))
is_prime = True
if number>1:
    for i in range(2,number):
        if (number%i)==0:
                is_prime = False
                break
print(is_prime)


