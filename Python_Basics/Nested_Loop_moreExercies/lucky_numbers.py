n = int(input())  # num from 1 - 9

num = n

for num1 in range(1, 10):
    for num2 in range(1, 10):
        for num3 in range(1, 10):
            for num4 in range(1, 10):
                if (num1 + num2) == (num3 + num4) and num % (num1 + num2) == 0:
                    print(f"{num1}{num2}{num3}{num4}", end=" ")
                else:
                    continue
