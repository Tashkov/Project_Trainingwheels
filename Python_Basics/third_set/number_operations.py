n1 = int(input())
n2 = int(input())
operator = input()
result = 0

if operator == "+":
    result = n1 + n2
elif operator == "-":
    result = n1 - n2
elif operator == "*":
    result = n1 * n2
elif operator == "/":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 / n2
        print(f"{n1} {operator} {n2} = {result:.2f}")
elif operator == "%":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    elif n2 != 0:
        result = n1 % n2
        print(f"{n1} {operator} {n2} = {result}")

if operator == "+" or operator == "-" or operator == "*":
    if result % 2 ==0:
        print(f"{n1} {operator} {n2} = {result} - even")
    elif result % 2 != 0:
        print(f"{n1} {operator} {n2} = {result} - odd")

