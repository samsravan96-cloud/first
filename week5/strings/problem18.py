user_string = input("Enter a sentence: ")
words = user_string.split() 
reversed_words = words[::-1]
print("Reversed order of words in the sentence:", ' '.join(reversed_words))