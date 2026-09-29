students = {101: 'Alice', 102: 'Bob', 103: 'Charlie', 104: 'David', 105: 'Eva', 106: 'Frank', 107: 'Grace', 108: 'Hannah'}
key_to_check = 105
if key_to_check in students:
    print(f"Key {key_to_check} exists with value: {students[key_to_check]}")
else:
    print(f"Key {key_to_check} does not exist in the dictionary.")