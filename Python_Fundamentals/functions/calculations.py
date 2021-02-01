operation = input()
num1 = int(input())
num2 = int(input())

def calculate(operator, y, z):
    result = None
    if operator == "multiply":
        result = y * z
    elif operator == "divide":
        result = y // z
    elif operator == "add":
        result = y + z
    elif operator == "subtract":
        result = y - z
    return result
print(calculate(operation,num1,num2))