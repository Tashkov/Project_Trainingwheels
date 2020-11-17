n = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(1, n + 1):
    number = int(input())
    if number < 200:
        p1 += 1
    elif 200 == number or number <= 399:
        p2 += 1
    elif 400 == number or number <= 599:
        p3 += 1
    elif 600 == number or number <= 799:
        p4 += 1
    elif number >= 800:
        p5 += 1

per1 = (p1 / n) * 100
per2 = (p2 / n) * 100
per3 = (p3 / n) * 100
per4 = (p4 / n) * 100
per5 = (p5 / n) * 100


print(f'{per1:.2f}%\n{per2:.2f}%\n{per3:.2f}%\n{per4:.2f}%\n{per5:.2f}%')
