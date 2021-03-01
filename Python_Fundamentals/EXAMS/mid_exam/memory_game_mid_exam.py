def insert_in_middle(array_numbers, number_moves):
    for iteration in range(2):
        middle = len(array_numbers) // 2
        element = f'-{number_moves}a'
        array_numbers.insert(middle, element)

    return array_numbers


sequence = [i for i in input().split()]
line = input()
moves_counter = 0

while not line == "end" and len(sequence) != 0:
    a, b = line.split()
    index1 = int(a)
    index2 = int(b)
    moves_counter += 1

    if index1 == index2 or index1 > len(sequence) - 1 or index2 > len(sequence) - 1 or index1 < 0 or index2 < 0:
        insert_in_middle(sequence, moves_counter)
        print("Invalid input! Adding additional elements to the board")
    else:
        if sequence[index1] == sequence[index2]:
            helper_list = [i for i in sequence]
            print(f"Congrats! You have found matching elements - {sequence[index1]}!")
            sequence.remove(helper_list[index1])
            sequence.remove(helper_list[index2])

        else:
            print('Try again!')

    if len(sequence) == 0:
        break
    else:
        line = input()

if len(sequence) == 0:
    print(f"You have won in {moves_counter} turns!")
elif len(sequence) != 0 and line == "end":
    print("Sorry you lose :(")
    print(*sequence, sep=" ")