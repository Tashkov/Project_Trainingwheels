factor = int(input())
count = int(input())

lst = list()

for i in range(1, 100000):
    if i % factor == 0:
        lst.append(i)
    if len(lst) == count:
        print(lst)
        exit()

