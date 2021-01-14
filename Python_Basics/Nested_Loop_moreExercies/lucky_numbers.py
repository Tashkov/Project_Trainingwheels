n = int(input())  # num from 1 - 9

num = n

for A in range(1, 10):
    for B in range(1, 10):
        for x in range(1, 10):
            for y in range(1, 10):
                if (A + B) == (x + y) and num % (A + B) == 0:
                    print(f"{A}{B}{x}{y}", end=" ")
                else:
                    continue
