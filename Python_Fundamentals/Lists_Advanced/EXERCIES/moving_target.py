sequence_of_targets = list(map(lambda x: int(x), input().split()))
line = input()

while line != "End":
    command = line.split()
    index = int(command[1])
    power = int(command[2])
    if command[0] == "Shoot":
        if index < len(sequence_of_targets):
            pass
    elif command[0] == "Add":
        pass
    elif command[0] == "Strike":
        pass
    line = input()