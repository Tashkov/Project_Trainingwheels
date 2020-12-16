from sys import maxsize

n = input()
max_number = -maxsize


while n != "Stop":
    number = int(n)
    if max_number < number:
        max_number = number
    n = input()
print(max_number)