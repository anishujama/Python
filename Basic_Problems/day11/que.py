#write a python program to sort a dictionary by value
a = {"a":12,"b":23,"c":6,"d":19,"e":91}
a = sorted(a.values())
print(a)
#write a python script to print dictionary where the keys are number between 1 abd 15 and the values are square of keys
a = {}
for i  in range (1,16):
    a[i]=i**2
print(a)    
#write a program to multiply all the item in a dictionary
a = {"a":12,"b":23,"c":6,"d":19,"e":91}
print (a["c"])
product = 1
for i in a:
    product*=a[i]
print(product)    
#write a python to sort a dictionary by key
a = {12:"a",23:"b",6:"c",19:"d",91:"e"}
a = sorted(a.keys())
print(a)