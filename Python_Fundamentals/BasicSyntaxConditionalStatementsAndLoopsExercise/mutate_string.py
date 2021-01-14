line1 = input()
line2 = input()

string_list1 = list(line1)
string_list2 = list(line2)
counter = 0

while string_list1 != string_list2:
    check1 = string_list1[counter]
    check2 = string_list2[counter]
    string_list1[counter] = string_list2[counter]

    if check1 != check2:
        new_string = "".join(string_list1)
        counter += 1
        print(new_string)
    else:
        counter += 1
        continue