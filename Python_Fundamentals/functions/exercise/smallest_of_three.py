num1 = int(input())
num2 = int(input())
num3 = int(input())

def smallest_number(x, y, z):
    number = 0
    if x < y and x < z:
        number = x
    else:
        if y < z:
            number = y
        else:
            number = z
    return number

print(smallest_number(num1, num2, num3))