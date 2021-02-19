array_integers = list(map(lambda x: int(x), input().split()))
line = input()

def exchange(array, index):
    if index > len(array):
        return "Invalid index"
    else:
        first_list = array[:index + 1]
        second_list = array[index + 1::]
        array_integers = second_list + first_list
        return array_integers

while line != "end":
    list_of_line = line.split()
    command = list_of_line[0]
    if command == "exchange":
        index = int(list_of_line[1])
        result = exchange(array_integers, index)
        if result == "Invalid index":
            print(result)
        else:
            array_integers = result

    elif command == "max":
        if list_of_line[1] == "even":
            look_trough = [digit for digit in array_integers if digit % 2 == 0]
            if len(look_trough) > 0:
                max_number = max(look_trough)
                print(array_integers.index(max_number))
            else:
                print("No matches")
        elif list_of_line[1] == "odd":
            look_trough = [digit for digit in array_integers if digit % 2 != 0]
            if len(look_trough) > 0:
                max_number = max(look_trough)
                print(array_integers.index(max_number))
            else:
                print("No matches")
    elif command == "min":
        if list_of_line[1] == "even":
            look_trough = [digit for digit in array_integers if digit % 2 == 0]
            if len(look_trough) > 0:
                min_number = min(look_trough)
                print(array_integers.index(min_number))
            else:
                print("No matches")

        elif list_of_line[1] == "odd":
            look_trough = [digit for digit in array_integers if digit % 2 != 0]
            if len(look_trough) >= 0:
                min_number = min(look_trough)
                print(array_integers.index(min_number))
            else:
                print("No matches")

    elif command == "first":
        cycles = int(list_of_line[1])
        even_odd = list_of_line[2]
        if cycles > len(array_integers):
            print("Invalid count")
        else:
            if even_odd == "even":
                list_to_print = []
                for digit in array_integers:
                    if digit % 2 == 0:
                        list_to_print.append(digit)
                        cycles -= 1
                        if cycles == 0:
                            break

                print(list_to_print)
            elif even_odd == "odd":
                list_to_print = []
                for digit in array_integers:
                    if digit % 2 != 0:
                        list_to_print.append(digit)
                        cycles -= 1
                        if cycles == 0:
                            break
                print(list_to_print)
    elif command == "last":
        cycles = int(list_of_line[1])
        even_odd = list_of_line[2]
        if cycles > len(array_integers):
            print("Invalid count")
        else:
            if even_odd == "even":
                list_to_print = []
                for ind_of_digit in range(-1, -len(array_integers), -1):
                    if int(array_integers[ind_of_digit]) % 2 == 0:
                        list_to_print.append(int(array_integers[ind_of_digit]))
                        cycles -= 1
                        if cycles == 0:
                            break
                print(list_to_print)
            elif even_odd == "odd":
                list_to_print = []
                for ind_of_digit in range(-1, -(len(array_integers)+1), -1):
                    if int(array_integers[ind_of_digit]) % 2 != 0:
                        list_to_print.append(int(array_integers[ind_of_digit]))
                        cycles -= 1
                        if cycles == 0:
                            break
                print(list_to_print)
    line = input()


if line == "end":
    print(array_integers)

