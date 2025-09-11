# WAP to create area calculator

print("*******AREA CALCULATOR******")
print("""press 1 to get the area of suare
press 2 to get the area of rectangle
 press 3 to get the area of circle 
 press 4 to get the area of triangle""")

choice = int(input("enter a number between 1-4: "))

if choice == 1:
    side = float(input("enter the length of the one side: "))
    area = side**2
    print("the area of suare is ", area)

elif choice == 2:
     length = float(input("enter the length of the rectangle: "))
     area = length * float(input("enter the width of the rectangle: "))
     print("the area of rectangle is ", area)
elif choice == 3:
     radius = float(input("enter the radius of the circle: "))
     area = 3.14 * radius ** 2
     print("the area of circle is ", area)

elif choice == 4:
     height = float(input("enter the height of the triangle: "))
     base = float(input("enter the base of the triangle: "))
     area = 0.5 * height * base
     print("the area of triangle is ", area)

else:
     print("invalid input")
