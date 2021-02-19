line = int(input())

def find_perfect_number(number):
    sum_of_divisors = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            sum_of_divisors += divisor
        else:
            continue
    if sum_of_divisors == number:
        print("We have a perfect number!")
    else:
        print("It`s not so perfect")
    return exit()

print(find_perfect_number(line))