initial_loot = [str(item) for item in input().split('|')]
line = input()

while not line == "Yohoho!":
    input_line = line.split()
    command = input_line[0]
    if command == "Loot":
        pass
    elif command == "Drop":
        pass
    elif command == "Steal":
        pass