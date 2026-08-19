character = str(input("Enter a character: "))

if ('a' <= character <= 'z') or ('A' <= character <= 'Z'):

    if (character == 'a' or character == 'e' or character == 'i' or
        character == 'o' or character == 'u' or character == 'A' or
        character == 'E' or character == 'I' or character == 'O' or
        character == 'U'):

        print("The character is a vowel.")

    else:
        print("The character is a consonant.")

else:
    if '0' <= character <= '9':
        print("The character is a digit.")
    else:
        print("The character is a special character.")