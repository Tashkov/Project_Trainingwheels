line = input()

lst = line.split()

for i in range(len(lst)):
    lst[i] = int(lst[i]) * -1

print(lst)