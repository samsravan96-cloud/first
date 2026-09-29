countries = ("USA", "Canada", "Mexico", "Brazil", "Argentina")
search_value = input("Enter a country name: ")

if search_value in countries:
    print("Value exists in the tuple.")
else:
    print("Value does not exist in the tuple.")