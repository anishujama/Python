#WAP to find a sum of all the even numbers upto 50
total = 0
for i in range (1,51):
    if i % 2 ==  0:
        total += i
    

print("the sum of all even number up to 50 is",total)
