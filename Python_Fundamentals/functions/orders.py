line = input()
quantity = int(input())

def waitress(order, amount):
    total = 0
    if order == "coffee":
        total += amount * 1.50
    elif order == "water":
        total += amount * 1.00
    elif order == "coke":
        total += amount * 1.40
    elif order == "snacks":
        total += amount * 2.00
    return f"{total:.2f}"

print(waitress(line, quantity))