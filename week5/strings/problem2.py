
user_string = input("Enter a string: ")
reversed_string = ""

for char in user_string:
    reversed_string = char + reversed_string

print("Reversed string (without slicing):", reversed_string)
print("Reversed string (with slicing):", user_string[::-1])