#wap to create an Area of calculator
# WAP to create area calculator

print("*******AREA CALCULATOR******")
while True:
     print("""press 1 to get the area of suare
     press 2 to get the area of rectangle
     press 3 to get the area of circle 
     press 4 to get the area of triangle""")

     choice = int(input("enter a number between 1-4: "))

     if choice == 1:
          while True:
               side = float(input("enter the length of the one side: "))
               area = side**2
               print("the area of suare is ", area)
               repeat = input("do you want to try with square? ")
               if repeat=="no":
                    break

     elif choice == 2:
          while True:
               length = float(input("enter the length of the rectangle: "))
               area = length * float(input("enter the width of the rectangle: "))
               print("the area of rectangle is ", area)
               repeat = input("do you want to try with rectangle? ")
               if repeat=="no":
                    break
     elif choice == 3:
          while True:
               radius = float(input("enter the radius of the circle: "))
               area = 3.14 * radius ** 2
               print("the area of circle is ", area)
               repeat = input("do you want to try with circle? ")
               if repeat=="no":
                    break

     elif choice == 4:
          while True:
               height = float(input("enter the height of the triangle: "))
               base = float(input("enter the base of the triangle: "))
               area = 0.5 * height * base
               print("the area of triangle is ", area)
               repeat = input("do you want to try with triangle? ")
               if repeat=="no":
                    break

     else: 
          print("invalid input")

     repeat1 = input("do you want repeat menu again? ")
     if repeat1=="no":
          break
