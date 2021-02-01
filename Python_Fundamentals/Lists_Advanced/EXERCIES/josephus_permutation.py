numbers = list(map(lambda x: int(x), input().split()))
k = int(input())
new_list = list(numbers)
result = []
while numbers != []:
    for index in range(k, len(numbers) + 1, k):
        number = numbers[index]
        if number in new_list:
            result.append(number)
            new_list.remove(number)
    print(result)