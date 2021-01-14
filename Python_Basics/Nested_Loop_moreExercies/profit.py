# Checks the alternative ways that you can return the sum_total
# depending on the amount of one, two and five leva.
one_lev = int(input())
two_lev = int(input())
five_lev = int(input())
sum_total = int(input())

for x in range(0, one_lev + 1):
    for y in range(0, two_lev + 1):
        for z in range(0, five_lev + 1):
            if (x * 1) + (y * 2) + (z * 5) == sum_total:
                print(f"{x} * 1 lv. + {y} * 2 lv. + {z} * 5 lv. = {sum_total} lv.")
                break
            else:
                continue
