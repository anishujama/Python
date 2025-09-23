#write a function to find maximu of thre numbers in python
def maximum_num (val1,val2,val3):
    if val1>val2 and val1>val3:
        print(val1,"is the greatest number")
    elif val2>val1 and val2>val3:
        print(val2,"is the greatest number")
    else:
        print(val3,"is the greatest number")
maximum_num(12,5,91)        
#write a python function to create and print a list where the value are square of number between 1 annd 130
def creare_list():
    L = []
    for i in range(1,31):
        L.append(i**2)
    return L
print(creare_list())
    

#write a python function that takes a number as a parameter and check if the number is prime or not
def check_prime(num):
    if num==1:
        print("it is not prime number")
    if num==2:
        print("it is prime number")
    if num>2:    
        for i in range(2,num):
            if num%i==0:
                print("it is not prime number")
                break
        else:
            print("it is prime number")
check_prime(37)            

#write a python function to sum all the numbers in a list
def add(numbers):
    total = 0
    for i in numbers:
        total = total+i
    return(total)
    
print(add([2,6,5,8]))    

#using recursion
def add(numbers):
    if len(numbers)==1:
        return (numbers[0])
    else:
        return ((numbers[0]) + add(numbers[1:]))

print(add([2,6,5,8]))

#wrie a python program to solve the fibonacci sequence using recursions

def fs(num):
    if num==1:
        return(0)
    elif num==2:
        return(1)
    else:
        return(fs(num-1)+fs(num-2))

print(fs(8))    