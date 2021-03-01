numbers = [int(num) for num in input().split()]
average = sum(numbers) / len(numbers)
top_five_numbers = []
numbers.sort(reverse=True)

counter = 5

for number in numbers:
    if number > average:
        counter -= 1
        top_five_numbers.append(number)
        if counter == 5:
            print("No")
            exit()
        elif counter == 0:
            break
if counter == 5:
    print("No")
else:
    print(*top_five_numbers, sep=" ")
