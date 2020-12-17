from math import floor, ceil

area = int(input())
grapes_per_square_m = float(input())
wine_liters_needed = int(input())
workers = int(input())
grapes_total = area * grapes_per_square_m
grapes_kg = (grapes_total * 0.4)
liters_wine_made = grapes_kg / 2.5

if liters_wine_made < wine_liters_needed:
    needed_wine = floor(wine_liters_needed - liters_wine_made)
    print(f'It will be a tough winter! More {needed_wine} liters wine needed.')
if liters_wine_made >= wine_liters_needed:
    wine_left = ceil(liters_wine_made - wine_liters_needed)
    workers_get = ceil(wine_left / workers)
    print(f"Good harvest this year! Total wine: {floor(liters_wine_made)} liters. "
          f"\n{wine_left} liters left -> {workers_get} liters per person.")
