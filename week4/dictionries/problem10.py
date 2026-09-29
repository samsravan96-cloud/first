
items = {"apple": 1.2, "banana": 0.8, "orange": 1.5, "grape": 2.0}
highest_item = max(items, key=items.get)
lowest_item = min(items, key=items.get)
print(f"Item with highest price: {highest_item} at ${items[highest_item]}")
print(f"Item with lowest price: {lowest_item} at ${items[lowest_item]}")