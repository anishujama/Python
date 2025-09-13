sentence = input("enter a sentence here:")
words = sentence.split()

for word in  words:
    i = len(word) - 1
    while i>=0:
        print(word[i],end="")
        i-=1
    print(end=" ")    