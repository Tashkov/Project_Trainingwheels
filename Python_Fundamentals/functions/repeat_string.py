line = input()
repeat_count = int(input())

def repeater(string, times):
    new_string = ""
    for i in range(times):
        new_string += string
    return new_string

print(repeater(line,repeat_count))