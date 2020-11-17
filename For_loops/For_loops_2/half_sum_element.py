from sys import maxsize

max_num = -maxsize
sum_numbers = 0

n = int(input())

for i in range(0, n):
    num = int(input())
    if num > max_num:
        max_num = num
    sum_numbers += num

if max_num == sum_numbers - max_num:
    print(f'Yes\nSum = {sum_numbers - max_num}')
else:
    sum_others = sum_numbers - max_num
    print(f'No\nDiff = {abs(max_num - sum_others)}')