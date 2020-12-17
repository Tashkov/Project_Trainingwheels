from math import ceil

fan_name = input()
budget = float(input())
number_bottles = int(input())
number_chips = int(input())

one_beer_price = 1.20
total_beers_price = number_bottles * one_beer_price
one_chips_price = (total_beers_price * 0.45)
total_chips_price = ceil(one_chips_price * number_chips)
total_money = total_chips_price + total_beers_price

if budget >= total_money:
    print(f"{fan_name} bought a snack and has {(budget - total_money):.2f} leva left.")
else:
    print(f"{fan_name} needs {(total_money - budget):.2f} more leva!")