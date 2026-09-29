dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Using update() method
dict1.update(dict2)
print("Merged dictionary using update():", dict1)

# Using | operator (Python 3.9+)
dict3 = {"a": 1, "b": 2}
dict4 = {"c": 3, "d": 4}
merged_dict = dict3 | dict4
print("Merged dictionary using | operator:", merged_dict)