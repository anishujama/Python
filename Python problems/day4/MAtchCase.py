x = int(input("enter the value of x:"))
match x:
    case 0:
        print("x is 0")
    case 1:
        print("x is 1")    
    case 2:
        print("x is 2")
    case 3:
        print("x is 3")    
    case 4:
        print("x is 4")
    case 5:
        print("x is 5")    
    case _ if x!=80:
        print(x,"x is not 80")    
    case _ if x!=90:
        print(x,"x is not 90")    
    case _ :
        print(x)    