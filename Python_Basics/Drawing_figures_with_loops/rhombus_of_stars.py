n = int(input())

for row in range(1, n + 1):
    print((n - row) * " " + "*" + (row - 1) * " *")

for row2 in range(n - 1, 0, -1):
    print((n - row2) * " " + "*" + (row2 - 1) * " *")
