hundreds = int(input())  # 1 - 9
tens = int(input())  # 1 - 9
ones = int(input())  # 1 - 9

for x in range(1, hundreds + 1):
    if x % 2 == 0:
        for y in range(2, tens + 1):
            for i in range(2, y):
                if y % i == 0:
                    break
            else:
                for z in range(1, ones + 1):
                    if z % 2 == 0:
                        print(f"{x} {y} {z}")
