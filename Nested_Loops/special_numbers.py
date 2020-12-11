number = int(input())
is_special_number = True

for i in range(1111, 10000):
    for index, value in enumerate(str(i)):
        if int(value) != 0 and number % int(value) != 0:
            is_special_number = False
            break
        if is_special_number:
            print(int(index), end=" ")
