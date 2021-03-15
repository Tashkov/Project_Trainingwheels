def place_in_alphabet(letter: str):
    looking_for = letter.lower()
    alphabet = {chr(num - 1): num - 97 for num in range(98, 124)}

    return int(alphabet[looking_for])

line = input().split()
# alphabet = {chr(num-1): num - 97 for num in range(98, 124)}
all_numbers = []
for word in line:
    first_operation = word[0]
    second_operation = word[-1]
    number_as_list = [char for char in word if char != first_operation and char != second_operation]
    number = float("".join(number_as_list))
    if first_operation.isupper():
        divisor = place_in_alphabet(first_operation)
        number /= divisor
    elif first_operation.islower():
        multiplier = place_in_alphabet(first_operation)
        number *= multiplier
    if second_operation.isupper():
        subtractor = place_in_alphabet(second_operation)
        number -= subtractor
    elif second_operation.islower():
        additor = place_in_alphabet(second_operation)
        number += additor
    all_numbers.append(number)

print(f"{sum(all_numbers):.2f}")