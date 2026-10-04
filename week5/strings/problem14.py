user_string = input("Enter a string: ")
substring = input("Enter a substring to check: ")
if substring in user_string:
    print(f"The substring '{substring}' exists in the string.")
else:
    print(f"The substring '{substring}' does not exist in the string.")