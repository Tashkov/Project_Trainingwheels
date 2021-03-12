list_of_strings = input().split()

n = 0
new_word = ""
for word in list_of_strings:
    n = len(word)
    new_word += word * n

print(new_word)
