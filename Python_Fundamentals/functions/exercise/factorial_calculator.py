num1 = int(input())
num2 = int(input())

def factorial_calculator(x, y):
    list1 = [el for el in range(1, x + 1)]
    list2 = [el for el in range(1, y + 1)]
    result1 = 1
    result2 = 1
    for i in range(-1, -len(list1), -1):
        result1 *= list1[i]
    for index in range(-1, -len(list2), -1):
        result2 *= list2[index]
    final_result = result1 / result2
    return f"{final_result:.2f}"

print(factorial_calculator(num1, num2))