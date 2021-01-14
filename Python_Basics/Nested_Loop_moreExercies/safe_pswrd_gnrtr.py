a = int(input())
b = int(input())
max_passwords = int(input())

first_symbol = 35
second_symbol = 64
for third_symbol in range(1, a + 1):
    for forth_symbol in range(1, b + 1):
        print(
            f"{chr(first_symbol)}{chr(second_symbol)}{third_symbol}{forth_symbol}{chr(second_symbol)}{chr(first_symbol)}",
            end="|")
        first_symbol += 1
        if first_symbol > 55:
            first_symbol = 35
        second_symbol += 1
        if second_symbol > 96:
            second_symbol = 64
        max_passwords -= 1
        if max_passwords == 0:
            exit()