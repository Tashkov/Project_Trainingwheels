n = int(input())

p2 = 0
p3 = 0
p4 = 0

for i in range(1, n + 1):
    number = int(input())
    if number % 2 == 0:
        p2 += 1
    if number % 3 == 0:
        p3 += 1
    if number % 4 == 0:
        p4 += 1
per2 = (p2 / n) * 100
per3 = (p3 / n) * 100
per4 = (p4 / n) * 100

print(f'{per2:.2f}%\n{per3:.2f}%\n{per4:.2f}%')