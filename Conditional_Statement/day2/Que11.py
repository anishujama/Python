#area of circle
import math
radius = float(input("enter radius of area:"))
if radius>0:
    area = math.pi*radius*radius
    print("area of circle is:",area)
else:
    print("cannot find ara of circle")
