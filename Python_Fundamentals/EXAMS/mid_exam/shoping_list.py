initial_list = input().split("!")
line = input()


def urgent(shopping_list, item):
    if item not in shopping_list:
        shopping_list.insert(0, item)

    return shopping_list


def unnecessary(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)

    return shopping_list


def correct(shopping_list, item, new_item):
    if item in shopping_list:
        index = shopping_list.index(item)
        shopping_list.pop(index)
        shopping_list.insert(index, new_item)
    return shopping_list

def rearrange(shopping_list, item):
    if item in shopping_list:
        index = shopping_list.index(item)
        shopping_list.pop(index)
        shopping_list.append(item)
    return shopping_list


while not line == "Go Shopping!":
    second_line = line.split()
    command = second_line[0]
    item = second_line[1]
    if command == "Urgent":
        initial_list = urgent(initial_list, item)
    elif command == "Unnecessary":
        initial_list = unnecessary(initial_list, item)
    elif command == "Correct":
        new_item = second_line[2]
        initial_list = correct(initial_list, item, new_item)
    elif command == "Rearrange":
        initial_list = rearrange(initial_list, item)

    line = input()

print(*initial_list, sep=", ")