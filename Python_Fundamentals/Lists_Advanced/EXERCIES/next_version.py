current_version = input().split(".")
string = ""

for i in range(len(current_version)):
    string += current_version[i]
number = int(string)

if number < 999:
    number += 1
    new_version = str(number)
    new_list = []
    for i in range(len(new_version)):
        new_list.append(new_version[i])
    result = "."
    result = result.join(new_list)
    print(result)
else:
    new_version = str(number)
    new_list = []
    for i in range(len(new_version)):
        new_list.append(new_version[i])
    result = "."
    result = result.join(new_list)
    print(result)
