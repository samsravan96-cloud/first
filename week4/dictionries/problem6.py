students = {101: 'Alice', 102: 'Bob', 103: 'Charlie', 104: 'David', 105: 'Eva', 106: 'Frank', 107: 'Grace', 108: 'Hannah'}
print("Keys:")
for key in students.keys():
    print(key)

print("Values:")
for value in students.values():
    print(value)

print("Key-Value Pairs:")
for key, value in students.items():
    print(f"{key}: {value}")