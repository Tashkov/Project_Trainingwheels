targets_to_be_shot = list(map(lambda x: int(x), input().split()))
command = input()
counter_shot_targets = 0

while not command == "End":
    index = int(command)
    current_target_value = 0
    if index < len(targets_to_be_shot):
        current_target_value = targets_to_be_shot[index]
        targets_to_be_shot[index] = -1
        counter_shot_targets += 1
        for i, number in enumerate(targets_to_be_shot):
            if targets_to_be_shot[i] != -1:
                if targets_to_be_shot[i] > current_target_value:
                    targets_to_be_shot[i] -= current_target_value
                elif targets_to_be_shot[i] <= current_target_value:
                    targets_to_be_shot[i] += current_target_value

    current_target_value = 0
    command = input()

print(f'Shot targets: {counter_shot_targets} -> ', end="")
for target in targets_to_be_shot:
    print(f'{target}', end=" ")
