items = input().split("|")
budget = float(input())

lst_sold_items = []
profit_price = 0
saved_sum = 0
profit_sum = 0

for selection in items:
    current_item = selection.split("->")
    item = current_item[0]
    price = float(current_item[1])

    if (item == "Clothes" and price <= 50.00 and price <= budget) or (item == "Shoes" and price <= 35.00 and price <= budget) or(item == "Accessories" and price <= 20.50 and price <= budget):
        budget -= price
        profit_price = price * 1.4
        saved_sum += profit_price
        lst_sold_items.append(profit_price)
        profit_sum += profit_price - price
    else:
        continue

saved_sum += budget

for stock in lst_sold_items:
    print(f'{stock:.2f}', end=" ")
print()
print(f'Profit: {profit_sum:.2f}')

if saved_sum >= 150:
    print('Hello, France!')
else:
    print('Time to go.')