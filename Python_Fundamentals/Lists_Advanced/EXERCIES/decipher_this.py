line = input().split()

new_list = [line]
number = ""
# converts string to list of its characters
def ConvertToList(string):
    list1 = []
    list1[:0] = string
    return list1

for i in range(len(line)):
    current_word = line[i]
    for char in ConvertToList(current_word):
        number += char
        print(char)

    print(current_word)

    print(number)
    number = ""




