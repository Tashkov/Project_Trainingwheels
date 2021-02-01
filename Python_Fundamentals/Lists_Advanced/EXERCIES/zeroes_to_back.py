line = list(map(lambda x: int(x), input().split(", ")))

add_number = 0

for number in line:
    if number == 0:
        line.remove(number)
        line.append(number)
print(line)