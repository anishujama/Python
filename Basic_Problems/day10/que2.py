#take an input from a user as a string then,rverse 

a = input("enter anything here: ")
print(a[::-1])

#wap to check if a string contains only digit

a = input("enter anything here: ")
b = a.isdigit()
if b==True:
    print("it contains only digit")
else:
    print("it does not contaon only digit")

#wap to check if a string is palindrome 

a = input("enter anything here: ")
rev = a[::-1]
if a == rev:
    print("string is palindrome")
else:
    print("string is not palindrome") 

#wap to find number of vowels in a string

a = input("enter anything here: ")
vowels = 0
for i in a:
    if i=="a" or i=="e" or i== "i" or  i =="o" or i == "u":
        vowels+=1
print("number of vowles in this string: ",vowels)  
      
#wap to check if every word in a string begins with a capital letter

a = input("enter anything here: ")
b = a.istitle()
print(b)
