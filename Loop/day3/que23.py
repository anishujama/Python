string = input("enter a string here:")
char_to_count = input("enter a character to check:")
count = 0
index = 0
while index<len(string):
    if string[index]==char_to_count:
        count+=1
    index+=1
print(f"{char_to_count} = {count}")