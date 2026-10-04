
user_string = input("Enter a string: ")
unique_characters = ""
for char in user_string:
    if char not in unique_characters:
        unique_characters += char
print("String with duplicate characters removed:", unique_characters)