num1 = int(input())  # num 1-9
num2 = int(input())  # num 1-9
num3 = int(input())  # num 1-9


for x in range(1, num1 + 1):
    if x % 2 == 0:
        for y in range(1, num2 + 1):
            if y in range(2, 8):
                for i in range(2, y + 1):
                    if (y % i) == 0 and y % 4 != 0 and y % 6 != 0:
                        for z in range(1, num3 + 1):
                            if z % 2 == 0:
                                print(x, y, z)
                    else:
                        continue
