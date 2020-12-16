from sys import maxsize
n = input()
min_number = maxsize

while n != "Stop":
    number = int(n)
    if number < min_number:
        min_number = number
    n = input()
print(min_number)