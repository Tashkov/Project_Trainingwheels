n = int(input())
numbers = 0

while numbers < n:
    num = int(input())
    numbers += num
    if numbers >= n:
        break
print(numbers)