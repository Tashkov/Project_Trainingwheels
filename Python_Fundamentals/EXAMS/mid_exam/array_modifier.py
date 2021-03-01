def swap(int_array: list, index1, index2):
    ints_to_swap = []
    ints_to_swap.append(int_array[index1])
    ints_to_swap.append(int_array[index2])
    int_array[index1] = ints_to_swap[1]
    int_array[index2] = ints_to_swap[0]

    return int_array


def multiply(int_array: list, index1, index2):
    to_be_saved = int_array[index1] * int_array[index2]
    int_array[index1] = to_be_saved

    return  int_array


def decrease(int_array: list):
    for i in range(0, len(int_array)):
        int_array[i] -= 1

    return int_array

initial_array = list(map(lambda x: int(x), input().split()))
line = input()

while not line == "end":
    command = line.split()
    action = command[0]
    if action == "swap":
        first_index = int(command[1])
        second_index = int(command[2])
        swap(initial_array, first_index, second_index)
    elif action == "multiply":
        first_index = int(command[1])
        second_index = int(command[2])
        multiply(initial_array, first_index, second_index)
    elif action == "decrease":
        decrease(initial_array)

    line = input()

print(*initial_array, sep=", ")