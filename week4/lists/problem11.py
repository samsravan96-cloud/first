#Create a list of numbers and demonstrate the use of append(), insert(), extend(), remove(), pop(), sort(), reverse(), count(), and index() methods, printing the list after each operation.

nums = [5, 2, 8, 1]

print("Initial list:", nums)

nums.append(7)
print("After append():", nums)

nums.insert(2, 9)
print("After insert():", nums)

nums.extend([4, 6])
print("After extend():", nums)

nums.remove(1)
print("After remove():", nums)

popped_value = nums.pop()
print("After pop():", nums, "Popped value:", popped_value)

nums.sort()
print("After sort():", nums)

nums.reverse()
print("After reverse():", nums)

print("Count of 2:", nums.count(2))
print("Index of 2:", nums.index(2))