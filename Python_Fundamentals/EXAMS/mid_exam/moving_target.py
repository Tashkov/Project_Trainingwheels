sequence_of_targets = list(map(lambda x: int(x), input().split()))
line = input()


def shoot(targets, index_of, power):
    if 0 <= index_of < len(targets):
        targets[index_of] -= power
        if targets[index_of] <= 0:
            targets.remove(targets[index_of])
    return targets


def add(targets, index_of, target):
    if 0 <= index_of < len(targets):
        targets.insert(index_of, target)
    else:
        return print("Invalid placement!")

    return targets


def strike(targets, index_of, radius):
    if 0 <= index_of < len(targets):
        if (index_of - radius) in range(len(targets)):
            del targets[index_of-radius:index_of+radius+1]
        else:
            return print("Strike missed!")
    else:
        return print("Strike missed")

    return targets


while not line == "End":
    command, index, amount = line.split()
    index = int(index)
    amount = int(amount)
    if command == "Shoot":
        shoot(sequence_of_targets, index, amount)
    elif command == "Add":
        add(sequence_of_targets, index, amount)
    elif command == "Strike":
        strike(sequence_of_targets, index, amount)

    line = input()

targets_int_to_str = [str(target) for target in sequence_of_targets]
str_of_targets = "|".join(targets_int_to_str)
print(str_of_targets)
