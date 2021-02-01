first_list = input().split(", ")
second_list = input()
result = []
for i in range(len(first_list)):
    found = second_list.find(first_list[i])
    if found != -1:
        result.append(first_list[i])
    else:
        continue

print(result)



