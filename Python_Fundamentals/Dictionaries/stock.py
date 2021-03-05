line_of_items = input().split()
items_to_look_for = [item for item in input().split()]
items_in_stock = {}

for i in range(0, len(line_of_items), 2):
    key = line_of_items[i]
    value = line_of_items[i + 1]
    items_in_stock[key] = int(value)

for item in items_to_look_for:
    if item in items_in_stock:
        print(f'We have {items_in_stock[item]} of {item} left')
    else:
        print(f'Sorry, we don`t have {item}')
