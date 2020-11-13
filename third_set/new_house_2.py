flowers = input()
quantity = int(input())
budget = int(input())
'''Flower types prices'''
roses = 5
dahlias = 3.80
tulips = 2.80
narcissus = 3
gladiolus = 2.5
total_price = 0

if flowers == "Roses" and quantity > 80:
    price = quantity * roses
    discount = price * 0.1
    total_price = price - discount
elif flowers == "Roses":
    total_price = quantity * roses

if flowers == "Dahlias" and quantity > 90:
    price = quantity * dahlias
    discount = price * 0.15
    total_price = price - discount
elif flowers == "Dahlias":
    total_price = quantity * dahlias

if flowers == "Tulips" and quantity > 80:
    price = quantity * tulips
    discount = price * 0.15
    total_price = price - discount
elif flowers == "Tulips":
    total_price = quantity * tulips

if flowers == "Narcissus" and quantity < 120:
    price = quantity * tulips
    discount = price * 0.15
    total_price = price + discount
elif flowers == "Narcissus":
    total_price = quantity * narcissus

if flowers == "Gladiolus" and quantity < 80:
    price = quantity * gladiolus
    discount = price * 0.2
    total_price = price + discount
elif flowers == "Gladiolus":
    total_price = quantity * gladiolus

if budget >= total_price:
    money_left = budget - total_price
    print(f"Hey, you have a great garden with {quantity} {flowers} and {(money_left):.2f} leva left.")
elif budget < total_price:
    money_needed = total_price - budget
    print(f"Not enough money, you need {(money_needed):.2f} leva more.")
