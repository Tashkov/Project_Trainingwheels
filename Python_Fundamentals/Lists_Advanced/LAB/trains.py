train_wagons = int(input())
train_lst = [0] * train_wagons
line = input()

while line != "End":
    command = line.split()
    key_word = command[0]
    if key_word == "add":
        train_lst[-1] += int(command[1])
    elif key_word == "insert":
        train_lst[int(command[1])] += int(command[2])
    elif key_word == "leave":
        train_lst[int(command[1])] -= int(command[2])
    line = input()

print(train_lst)
