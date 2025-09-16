a =["Thor","Hulk","Ironman","Captain america",]
#to find the of a list
print(len(a))
#to count an accurence of a particular elemennt
print(a.count("Thor"))
#to add the list
a.append("modi")
print(a)
#to add to a specific location
a.insert(1,"modi")
print(a)
#to remove  from a list
a.remove("Hulk")
print(a)
#to remove form a certaion location
a.pop(3)
#to create a copy of a list
b = a.copy()
print(b)
#to access an element
print(a.index("Thor"))
#to entent the list
v = ["shaikh", "obama"]
a.extend(v)
print(a)
#to reverse the list
a.reverse()
print(a)
#to  sort the list
a.sort()
print(a)
#to clear all the data from the list
print(a.clear())
print(a)
#wap to swap first and fourth element
a[0],a[3] = a[3],a[0]
print(a)
#wap to add new value at second position
a.insert(1,"shelby")
print(a)
#wap to delete a value from 3rd position
a.pop(2)
print(a)
"*************New Question************"
B = [13,7,12,10]
#wap to multiply all the number in the list
mul = 1
for i in (B):
    mul*=i
print(mul)    
#wap to get the largest number form the list
B.sort()
print(B)
print("The largest element is:",B[-1])
#wap to get the shortest number form the list
B.sort()
print(B)
print("The smallest element is:",B[0])
