numbers = input().split()
num_to_remove = int(input())

# converts the values of the indexes from str to int
for i in range(0, len(numbers)):
    numbers[i] = int(numbers[i])
# removes the smallest value from the list
for n in range(1, num_to_remove + 1):
    digit_to_remove = min(numbers)
    numbers.remove(digit_to_remove)

print(numbers)



