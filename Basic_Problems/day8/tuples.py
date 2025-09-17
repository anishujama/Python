mytuple = ("ronaldo","messi","neymar")
print(mytuple[2])
if "messi" in mytuple:
    print("yes")
else:
    print("no")

mylist = list(mytuple)

mylist[0] ="putin"

print("updated list:",mylist)

mytuple = tuple(mylist)
print(mytuple)