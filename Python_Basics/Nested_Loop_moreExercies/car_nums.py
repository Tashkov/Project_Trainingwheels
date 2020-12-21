interval_start = int(input())  # num btw 1 - 9
interval_end = int(input())  # num btw 1 - 9

for num1 in range(interval_start, interval_end + 1):
    for num2 in range(interval_start, interval_end + 1):
        for num3 in range(interval_start, interval_end + 1):
            for num4 in range(interval_start, interval_end + 1):
                if num1 % 2 == 0 and num4 % 2 !=0:
                    if num1 > num4:
                        if (num2 + num3) % 2 == 0:
                            print(f"{num1}{num2}{num3}{num4}", end=" ")

                        else:
                            continue
                    else:
                        continue
                elif num1 % 2 != 0 and num4 % 2 ==0:
                    if num1 > num4:
                        if (num2 + num3) % 2 == 0:
                            print(f"{num1}{num2}{num3}{num4}", end=" ")

                        else:
                            continue
                    else:
                        continue
                else:
                    continue
