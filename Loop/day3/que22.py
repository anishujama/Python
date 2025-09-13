num  = int(input("enter number here:"))
i = 1
is_perfect_square = False
while i*i<=num:
    if i*i==num:
        is_perfect_square =True
        break
    i+=1
if is_perfect_square:
    print(f"{num} is perfect square")
else:
    print(f"{num} is not perfect square")    
