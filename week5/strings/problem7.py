def count_character(string, character):
    count = 0
    for char in string:
        if char == character:
            count += 1
    return count    

user_string = input("Enter a string: ")
character = input("Enter a character to count: ")
result = count_character(user_string, character)
print(f"The character '{character}' appears {result} times in the string.")