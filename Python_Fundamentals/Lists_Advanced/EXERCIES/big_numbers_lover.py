numbers = input().split()
string = ""
numbers.sort(reverse=True)
for number in numbers:
    string += number
print(string)


