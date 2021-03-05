products_in_stock = {}
line = input()

while not line == "statistics":
    tokens = line.split(":")
    key = tokens[0]
    quantity = int(tokens[1])
    if key in products_in_stock:
        products_in_stock[key] += quantity
    else:
        products_in_stock[key] = quantity

    line = input()

key_sum = 0
value_sum = 0
print("Products in stock:")
for key, value in products_in_stock.items():
    key_sum += 1
    value_sum += value
    print(f"- {key}: {value}")
print(f"Total Products: {key_sum}")
print(f"Total Quantity: {value_sum}")
