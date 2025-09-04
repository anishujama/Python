#pythagorean

a= int(input())
b= int(input())
c= int(input())

if (a*a+b*b==c*c )or (b*b+ c*c== a*a) or (a*a+c*c==b*b):
    print(1)
else:
    print(0)
    