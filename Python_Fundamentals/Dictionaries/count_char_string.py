line = input().split()
dictionary = {}

for word in line:
    for char in word:
        if char not in dictionary:
            dictionary[char] = 1
        else:
            dictionary[char] += 1
for key, value in dictionary.items():
    print(f"{key} -> {value}")