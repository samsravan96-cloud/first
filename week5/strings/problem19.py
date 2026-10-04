user_string = input("Enter a sentence: ")
words = user_string.split()
capitalized_words = [word.capitalize() for word in words]
print("Title case of the sentence:", ' '.join(capitalized_words))