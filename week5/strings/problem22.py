 #Check if a string contains only digits, only alphabets, or is alphanumeric.
user_string = input("Enter a string: ")

if user_string.isdigit():
    print("The string contains only digits.")
elif user_string.isalpha():
    print("The string contains only alphabets.")
elif user_string.isalnum():
    print("The string is alphanumeric.")
else:
    print("The string contains characters other than digits, alphabets, or both.")