#pet food recomendation

pet = input("Enter name of your pet:")
age= int(input("enter the age of your pet:"))

if pet=="dog":
    if age<=2:
        print("We recomendded puppy food for your pet")
elif pet == "cat":
     if age>=5:
         print("We recomendded semior cat food for your pet")
else:
    print("please enter valid pet name also valid age")