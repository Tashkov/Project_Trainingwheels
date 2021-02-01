gifts = input().split()
command = input()

help_list = []
while command != "No Money":
    current_command = command.split()
    current_gift = current_command[1]
    # this works
    if current_command[0] == "OutOfStock":
        for index in range(len(gifts)):
            if gifts[index] == current_gift:
                gifts[index] = "None"
    # this works
    elif current_command[0] == "Required":
        current_index = int(current_command[2])
        if 0 <= current_index < len(gifts):
            gifts[current_index] = current_gift
    elif current_command[0] == "JustInCase":
        gifts[-1] = current_gift
    # we end the cycle here
    command = input()

for gift in gifts:
    if gift != "None":
        print(gift, end=" ")
