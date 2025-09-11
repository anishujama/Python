#write a program check whether the passed letter is a vowel or not
letter = input("enter a letter here:")
if letter in "aeiou" or (letter in"AEIOU"):
    print("it is a vowel")
else:
    print("it is not vowels")