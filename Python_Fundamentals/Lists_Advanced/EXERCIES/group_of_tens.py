numbers = list(map(lambda x: int(x), input().split(", ")))

list_numbers = list(numbers)
current_list = []

max_value = 0

while list_numbers != []:
    max_value += 10
    current_list = []
    for number in numbers:
        if number <= max_value and number in list_numbers:
            current_list.append(number)
            list_numbers.remove(number)
    print(f'Group of {max_value}`s: {current_list}')

