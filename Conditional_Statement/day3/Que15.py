#ATM
x,y=input().split()
x=int(x)
y= float(y)

if(x>0 and x<2000) and (y>0 and y<2000):
    if x%5==0 and x<=y:
        z = y-(x+0.5)
        print(f'%.2f'%z)
    else:
        print(f'%2f'%y)
