n = int(input())
odd_sum = 0
even_sum = 0

for i in range(1, n + 1):
    element = int(input())
    if i % 2 == 0:
        even_sum += element
    else:
        odd_sum += element
if odd_sum == even_sum:
    print(f'Yes\nSum = {odd_sum}')
else:
    print(f'No\nDiff = {abs(odd_sum - even_sum)}')