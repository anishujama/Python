# Reversed string

input_string = input()
reversed_string = ""
for char in input_string:
    reversed_string = char + reversed_string
print(reversed_string)   