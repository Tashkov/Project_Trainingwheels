A = int(input())  # num 1-9
B = int(input())  # num 1-9
x = int(input())  # num 1-9


for x in range(1, A + 1):
    if x % 2 == 0:
        for y in range(1, B + 1):
            if y in range(2, 8):
                for i in range(2, y + 1):
                    if (y % i) == 0 and y % 4 != 0 and y % 6 != 0:
                        for z in range(1, x + 1):
                            if z % 2 == 0:
                                print(x, y, z)
                    else:
                        continue
