num1 = int(input())
num2 = int(input())
num3 = int(input())

def sum_numbers(first_num, second_num):
    result = first_num + second_num
    return result

def subtract(result_of_sum, subtractor_num):
    result = result_of_sum - subtractor_num
    return result

def add_and_subtract(first_num, second_num, third_num):
    result = subtract(sum_numbers(first_num, second_num), third_num)
    return result

print(add_and_subtract(num1, num2, num3))

