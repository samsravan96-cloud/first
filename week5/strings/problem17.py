user_string = input("Enter a sentence: ")
words = user_string.split()
longest_word = max(words, key=len)
print("Longest word in the sentence:", longest_word)