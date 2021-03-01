def adding(sugar: list, amount: int):
    sugar.append(amount)

    return sugar


def remove(sugar: list, amount: int):
    for element in sugar:
        if element == amount:
            sugar.remove(element)
            break

    return sugar


def replace(sugar: list, amount: int, replacement: int):
    look_through_list = [el for el in sugar]
    for element in look_through_list:
        if element == amount:
            index_of_element = look_through_list.index(amount)
            sugar.pop(index_of_element)
            sugar.insert(index_of_element, replacement)
            break

    return sugar


def collapse(sugar: list, amount: int):
    look_through_list = [el for el in sugar]
    for element in look_through_list:
        if element < amount:
            sugar.remove(element)

    return sugar


count_of_sugars = [int(sugar) for sugar in input().split()]
line = input()

while not line == "Mort":
    line2 = line.split()
    command = line2[0]
    value = int(line2[1])
    if command == "Add":
        adding(count_of_sugars, value)
    elif command == "Remove":
        remove(count_of_sugars, value)
    elif command == "Replace":
        replacement = int(line2[2])
        replace(count_of_sugars, value, replacement)
    elif command == "Collapse":
        collapse(count_of_sugars, value)

    line = input()

print(*count_of_sugars, sep=" ")
