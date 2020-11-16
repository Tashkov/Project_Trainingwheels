lst_1 = []
lst_2 = []
n = int(input())

for i in range(n):
    number = int(input())
    lst_1.append(number)
for i in range(n):
    number = int(input())
    lst_2.append(number)

sum1 = sum(lst_1)
sum2 = sum(lst_2)

if sum1 == sum2:
    print(f'Yes, sum = {sum1}')
elif sum1 > sum2 or sum1 < sum2:
    print(f'No, diff = {abs(sum1 - sum2)}')
