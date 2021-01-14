star_of_interval = int(input())  # 1 - 999
end_of_interval = int(input())  # bigger than start_of_interval - 1000
magic_number = int(input())  # 1 - 10000

counter = 0
first_number = 0
second_number = 0

for num1 in range(star_of_interval, end_of_interval + 1):
    for num2 in range(star_of_interval, end_of_interval + 1):
        counter += 1
        if num1 + num2 == magic_number:
            first_number = num1
            second_number = num2
            break
    if first_number + second_number == magic_number:
        break
if first_number + second_number == magic_number:
    print(f"Combination N:{counter} ({first_number} + {second_number} = {magic_number})")
else:
    print(f"{counter} combinations - neither equals {magic_number}")