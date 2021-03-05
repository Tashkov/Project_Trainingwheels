line = input()
products_dictionary = {}

while not line == "buy":
    token = line.split()
    list_values = []
    product = token[0]
    price = float(token[1])
    quantity = int(token[2])
    list_values.append(price)
    list_values.append(quantity)
    if product not in products_dictionary:
        products_dictionary[product] = list_values
    else:
        products_dictionary[product][0] = price
        products_dictionary[product][1] += quantity

    line = input()

for key, value in products_dictionary.items():
    total_price = value[0] * value[1]
    print(f"{key} -> {total_price:.2f}")