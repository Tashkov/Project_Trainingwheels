divisor = int(input())
bound = int(input())

largest = 0

for i in range(divisor, bound + 1):
    if i % divisor == 0 and 0 < i <= bound:
        if i > largest:
            largest = i

print(largest)