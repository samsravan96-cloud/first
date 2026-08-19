n = 4

# Upper part
for i in range(1, n + 1):
    print("* " * i + " " * (4 * (n - i)) + "* " * i)

# Lower part
for i in range(n, 0, -1):
    print("* " * i + " " * (4 * (n - i)) + "* " * i)