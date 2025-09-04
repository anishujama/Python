'''fruit ripeness checker 
determint if a fruit is ripe , ovrerripe 
or unique based on its color
eg, banana - green - unripe
yellow - ripe - browm - overripe
'''
fruit = "Banana"
color = input("enter color of fruit:")

if fruit=="Banana":
    if color=="green":
        print("unripe")
    elif color=="yellow":
        print("ripe")
    elif color=="brown":
        print("overripe")
    else:
        print("color is not matched")

