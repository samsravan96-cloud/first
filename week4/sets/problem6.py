set1 = {1, 2, 3, 4, 5}
set1.remove(3)  # Removes element 3 from the set
# If element 3 did not exist in the set, this would raise a KeyError
print("Set after remove():", set1)

set1.discard(6)  # Removes element 6 from the set if it exists
# If element 6 did not exist in the set, this would not raise an error
print("Set after discard():", set1)