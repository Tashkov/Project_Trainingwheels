line = int(input()) + 1

while len(set(str(line))) != len(str(line)):
    line += 1

print(line)
# breaks judge 60/100
