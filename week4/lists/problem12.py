# Example list with duplicate values
lst = [1, 2, 2, 3, 4, 4, 5, 3]

unique_list = []

for value in lst:
    if value not in unique_list:
        unique_list.append(value)

print("Original list:", lst)
print("List without duplicates:", unique_list)