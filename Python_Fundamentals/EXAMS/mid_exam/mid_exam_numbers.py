numbers = [int(num) for num in input().split()]
average = sum(numbers) / len(numbers)
top_five_numbers = []
counter = 5

for number_id in range((len(numbers) - 1), 0, -1):
    if numbers[number_id] > average:
        counter -= 1
        top_five_numbers.append(numbers[number_id])
        if counter == 5:
            print("No")
            break
        elif counter == 0:
            print(*numbers, sep=" ")
            break

print(*numbers, sep=" ")
