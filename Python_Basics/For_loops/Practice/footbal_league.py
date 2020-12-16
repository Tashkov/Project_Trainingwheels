capacity = int(input())
fans = int(input())
sum_fans = 0
sec_a = 0
sec_b = 0
sec_v = 0
sec_g = 0

for i in range(fans):
    sector = input()
    sum_fans += 1
    if sector == "A":
        sec_a += 1
    elif sector == "B":
        sec_b += 1
    elif sector == "V":
        sec_v += 1
    elif sector == "G":
        sec_g += 1

print(f'{sec_a / sum_fans * 100:.2f}%\n'
      f'{sec_b / sum_fans * 100:.2f}%\n'
      f'{sec_v / sum_fans * 100:.2f}%\n'
      f'{sec_g / sum_fans * 100:.2f}%\n'
      f'{sum_fans / capacity * 100:.2f}%')