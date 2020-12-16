n1 = int(input())
n2 = int(input())
magic_number = int(input())
total_combinations = 0
is_found = False

for x1 in range(n1, n2 + 1):
    for x2 in range (n1, n2 + 1):
        total_combinations += 1
        if x1 + x2 == magic_number:
            print(f"Combination N:{total_combinations} ({x1} + {x2} = {magic_number})")
            is_found = True
            break
    if is_found:
        break
if is_found == False:
    print(f"{total_combinations} combinations - neither equals {magic_number}")