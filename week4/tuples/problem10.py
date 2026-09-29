immutable_tuple = ("a", "b", "c")

try:
    immutable_tuple[0] = "x"
except TypeError as error:
    print("Error:", error)