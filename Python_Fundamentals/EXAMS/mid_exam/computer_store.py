line = input()
list_prices = []

while line != "special" and line != "regular":
    price = float(line)
    if price < 0:
        print("Invalid price!")
    else:
        list_prices.append(price)

    line = input()

price_without_taxes = sum(list_prices)
VAT_tax = price_without_taxes * 0.2
total_price = price_without_taxes + VAT_tax

if total_price == 0:
    print("Invalid order!")
    exit()
if line == "special":
    total_price *= 0.9

print("Congratulations you've just bought a new computer!")
print(f"Price without taxes: {price_without_taxes:.2f}$")
print(f"Taxes: {VAT_tax:.2f}$")
print("-----------")
print(f"Total price: {total_price:.2f}$")