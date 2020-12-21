line1 = input()  # beginning of th interval
line2 = input()  # end of the interval
line3 = input()  # letter to not be included
# 97 - 122 =  a - z in ASCII
char1 = ord(line1)
char2 = ord(line2)
char3 = ord(line3)
counter = 0

for x in range(char1, char2 + 1):
    for y in range(char1, char2 + 1):
        for z in range(char1, char2 + 1):
            if x != char3 and y != char3 and z != char3:
                counter += 1
                print(chr(x) + chr(y) + chr(z), end=" ")
            else:
                continue

print(counter, end=" ")
