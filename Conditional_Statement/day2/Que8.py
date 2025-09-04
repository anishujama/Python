#password strength checker
password = (input("Enter your password:"))
   
if len (password) <= 6 :
    print("your password strength is weak")
elif len(password) > 6 and len(password)<=10:
    print("your password strength is medium")
else:
    print("your password is strong")