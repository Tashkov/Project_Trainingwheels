number = input()
combo_number = 1

list = []
new_number = 0

for i in range(1, len(number) + 1):
    combo_number *= i

while int(number) < new_number:
