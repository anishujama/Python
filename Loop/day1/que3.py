#multiplication table printer

number = int(input())
for i in range (1,10):
    if i ==5:
        continue
    print(number,'x',i,'=', number * i)  
