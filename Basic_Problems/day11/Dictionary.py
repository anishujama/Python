 #Iteration in dictionaries 
student = {"name":"John","Class":"6th","roll_no":23}
 
#printing all the key name one by one
for x in student:
    print(x)
#printing the all the value names one by one
for x in student:
    print(student[x])

#using value function
for x in student.values():
    print(x)
#using item function
for x,y in student.items():
    print(x,":",y)

#get
x = student.get("Class")
print(x)
#item
x = student.items()
print(x)
#keys
x = student.keys()
print(x)
#values
x = student.values()
print(x)
#copy
x = student.copy()
print(x)


# 1. setdefault
student.setdefault("age", 12)   
print(student)   

# 2. update
student.update({"Class": "7th"})
print(student)

# 3. pop
student.pop("roll_no")  
print(student)  

# 4. popitem
student.popitem()  
print(student)    