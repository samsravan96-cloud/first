numbers = [-5, 2, -8, 10, 0, -1]
updated_numbers = [0 if num < 0 else num for num in numbers]
print(updated_numbers)