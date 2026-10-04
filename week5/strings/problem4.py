user_string = input("Enter a string: ")

is_palindrome = True

for i in range(len(user_string) // 2):
    if user_string[i] != user_string[len(user_string) - 1 - i]:
        is_palindrome = False
        break

if is_palindrome:
    print("The string is a palindrome.")
else:
    print("not string palindrom" )