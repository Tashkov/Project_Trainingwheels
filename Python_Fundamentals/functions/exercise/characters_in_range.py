char1 = ord(input())
char2 = ord(input())

def char_in_range(start, end):
    string = ""
    for num in range(start + 1, end):
        string += chr(num) + " "
    return string

print(char_in_range(char1, char2))