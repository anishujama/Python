# Transport mode  selection
distance = int(input("Enter distance in km :"))
if distance<3:
    Transport = "you go with walk"
elif distance<3 and distance>15:
    Transport = "you go with bike"
else:
    Transport="you go with car"
print(Transport)    