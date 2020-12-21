n = int(input())  # the user writes one integer

counter = 0
number = 0

for i in range(n):
    num = int(input())
    number += num
    counter += 1

print(f"{number / counter:.2f}")
