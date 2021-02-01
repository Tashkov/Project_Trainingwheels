n1 = int(input())
n2 = int(input())
list_of_numbers = input()
result = 0

if list_of_numbers == "+":
    result = n1 + n2
elif list_of_numbers == "-":
    result = n1 - n2
elif list_of_numbers == "*":
    result = n1 * n2
elif list_of_numbers == "/":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 / n2
        print(f"{n1} {list_of_numbers} {n2} = {result:.2f}")
elif list_of_numbers == "%":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    elif n2 != 0:
        result = n1 % n2
        print(f"{n1} {list_of_numbers} {n2} = {result}")

if list_of_numbers == "+" or list_of_numbers == "-" or list_of_numbers == "*":
    if result % 2 ==0:
        print(f"{n1} {list_of_numbers} {n2} = {result} - even")
    elif result % 2 != 0:
        print(f"{n1} {list_of_numbers} {n2} = {result} - odd")

