text = input()
new_sequence = ""
for index in range(0, len(text)):
    if not index + 1 > len(text) - 1:
        if text[index] != text[index+1]:
            new_sequence += text[index]
    else:
        new_sequence += text[-1]

print(new_sequence)