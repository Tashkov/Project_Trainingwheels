interval_start = int(input())  # num btw 1 - 9
interval_end = int(input())  # num btw 1 - 9

for A in range(interval_start, interval_end + 1):
    for B in range(interval_start, interval_end + 1):
        for x in range(interval_start, interval_end + 1):
            for y in range(interval_start, interval_end + 1):
                if A % 2 == 0 and y % 2 !=0:
                    if A > y:
                        if (B + x) % 2 == 0:
                            print(f"{A}{B}{x}{y}", end=" ")

                        else:
                            continue
                    else:
                        continue
                elif A % 2 != 0 and y % 2 ==0:
                    if A > y:
                        if (B + x) % 2 == 0:
                            print(f"{A}{B}{x}{y}", end=" ")

                        else:
                            continue
                    else:
                        continue
                else:
                    continue
