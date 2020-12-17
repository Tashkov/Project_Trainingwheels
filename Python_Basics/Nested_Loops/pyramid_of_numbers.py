number = int(input())
current = 1
check = False

for row in range (1, number + 1):
    for col in range(1, row + 1):

        if current > number:
            check = True
            break
        print(" ","*"," ", end="")
        current += 1
    if check:
        break
    print()