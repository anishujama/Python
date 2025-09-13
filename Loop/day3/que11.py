# count vowels in word

vowels = "aeiou"
word = input()
count =0
for char in word:
    if char in vowels:
        count +=1 
print(f"vowel in {word} is: {count}")        
  
