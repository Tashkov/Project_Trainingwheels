from math import floor, ceil

days = int(input())
food = int(input())
dog_food_day_kg = float(input())
cat_food_day_kg = float(input())
turtle_food_day_kg = float(input())

dog_eats = dog_food_day_kg * days
cat_eats = cat_food_day_kg * days
turtle_eats = (turtle_food_day_kg / 1000 ) * days
animals_eat = dog_eats + cat_eats + turtle_eats

if animals_eat <= food:
    left = floor(food - animals_eat)
    print(f'{left} kilos of food left.')
else:
    lack = ceil(animals_eat - food)
    print(f'{lack} more kilos of food are needed.')