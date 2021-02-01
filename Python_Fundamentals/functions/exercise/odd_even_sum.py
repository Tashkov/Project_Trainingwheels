number_as_string = input()

def odd_even_sum(num):
    odd_sum = 0
    even_sum = 0
    for index in range(len(num)):
        if int(num[index]) % 2 == 0:
            even_sum += int(num[index])
        else:
            odd_sum += int(num[index])
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"

print(odd_even_sum(number_as_string))