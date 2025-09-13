word = input("enter a word to check :")
vowels = "aeiou"
count = 0
index = 0
while index<len(word):
    if word[index].lower() not in vowels and word[index].isalpha():
        count +=1
    index +=1
print(count)     