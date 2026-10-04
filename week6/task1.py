
import re
sentence = "1024 requests were served in 3 seconds"
pattern = r"\d"

if re.match(pattern, sentence):
    print("The sentence starts with a digit.")
else:
    print("The sentence does not start with a digit.")


match = re.search(r"served", sentence)
if match:
    print(f"The word 'served' is found at position {match.span()}.")


if re.fullmatch(r"\d+", "12345"):
    print("The string '12345' consists only of digits.")

if re.fullmatch(r"\d+", "123a5"):
    print("The string '123a5' consists only of digits.")
else:
    print("The string '123a5' contains non-digit characters.")