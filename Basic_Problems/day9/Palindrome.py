#wap to find a palindrome of integers
num =int(input("enter a number here:"))
temp = num
rev = 0
while num>0:
    dig = num%10
    rev= rev*10+dig
    num = num//10
if rev==temp:
    print("it is palindrome number")
else:
    print("it is not palindrome number")