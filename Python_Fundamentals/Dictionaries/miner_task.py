line = input()
counter = 0
dictionary = {}
resource = ""
quantity = 0
while not line == "stop":
    counter += 1
    if counter % 2 != 0:
        resource = line
        if resource not in dictionary:
            dictionary[resource] = 0
    else:
        quantity = int(line)
        dictionary[resource] += quantity

    line = input()

for key, value in dictionary.items():
    print(f"{key} -> {value}")
