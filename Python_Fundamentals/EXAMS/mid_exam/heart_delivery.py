neighborhood = list(map(lambda x: int(x), input().split("@")))
command = input()
cupid_jumps = []

while command != "Love!":
    list_of_commands = command.split()
    current_index = int(list_of_commands[1])
    cupid_jumps.append(current_index)
    if len(cupid_jumps) == 1:
        neighborhood[cupid_jumps[0]] -= 2

    else:
        if cupid_jumps[-2] + current_index > len(neighborhood):
            neighborhood[0] -= 2
        else:
            neighborhood[cupid_jumps[-2] + current_index] -= 2

    command = input()

print(neighborhood)
print(cupid_jumps)

