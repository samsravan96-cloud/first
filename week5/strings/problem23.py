user_string = input("Enter a string: ")
duplicate_chars = {}

for char in user_string:
    duplicate_chars[char] = duplicate_chars.get(char, 0) + 1

# Filter out characters that appear only once
duplicate_chars = {char: count for char, count in duplicate_chars.items() if count > 1}

print("Duplicate characters and their counts:")
for char, count in duplicate_chars.items():
    print(f"'{char}': {count}")