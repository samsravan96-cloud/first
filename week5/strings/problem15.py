user_string = input("Enter a string: ")
character = input("Enter a character to find: ")
first_index = user_string.find(character)
last_index = user_string.rfind(character)
if first_index != -1:
    print(f"First occurrence of '{character}': Index {first_index}")
else:
    print(f"Character '{character}' not found in the string.")

if last_index != -1:
    print(f"Last occurrence of '{character}': Index {last_index}")
else:
    print(f"Character '{character}' not found in the string.")