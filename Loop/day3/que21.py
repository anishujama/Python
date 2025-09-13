base = int(input("enter a base value:"))
exponent = int(input("enter exponenet number:"))

#power_Value = base**exponent
power_Value = 1
count = 0
while count<exponent:
    power_Value*=base
    count+=1
print(power_Value)    
#print(power_Value)