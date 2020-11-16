lst = []
n = int(input())

for i in range(n):
    number = int(input())
    lst.append(number)
odd = sum(lst[0::2])
even= sum(lst[1::2])

if odd == even:
    print(f'Yes\nSum = {odd}')
else:
    print(f'No\nDiff = {abs(odd - even)}')



