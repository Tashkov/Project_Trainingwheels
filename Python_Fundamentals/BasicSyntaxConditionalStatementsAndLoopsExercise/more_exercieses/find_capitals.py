word = input()

list = []

for i in range(len(word)):
    letter = word[i]
    if letter.isupper() == True:
        list.append(i)
print(list)