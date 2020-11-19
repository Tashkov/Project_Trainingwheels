n = int(input())

current_sum = 0
previous_sum = 0

for i in range(1, n + 1):
    n1 = int(input())
    n2 = int(input())
    if i % 2 == 0:
        current_sum = n1 + n2
    elif i % 2 != 0:
        previous_sum = n1 + n2


if current_sum > previous_sum and n > 1:
   a = current_sum - previous_sum
   print(f"No, maxdiff={a}")
elif previous_sum > current_sum and n > 1:
   a = previous_sum - current_sum
   print(f"No, maxdiff={a}")
elif current_sum == previous_sum and n > 1:
   print(f"Yes, value={current_sum}")
else:
    print(f"Yes, value={previous_sum}")
