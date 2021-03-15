line = input()

index = 0
partial_string = ""
result = ""

while index < len(line):

    if not line[index].isdigit():
        partial_string += line[index]
        index += 1
    else:
        repeater = ""
        while line[index].isdigit():
            repeater += line[index]
            index += 1
            if index == len(line):
                break
        repeater = int(repeater)
        output = partial_string.upper() * repeater
        result += output
        partial_string = ""


print(f"Unique symbols used: {len(set(result))}")
print(result)
