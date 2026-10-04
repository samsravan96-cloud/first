# Replace all occurrences of a character/word with another.
user_string = input("Enter a string: ")
old_character = input("Enter the character/word to replace: ")
new_character = input("Enter the new character/word: ")
modified_string = user_string.replace(old_character, new_character)
print("Modified string:", modified_string)