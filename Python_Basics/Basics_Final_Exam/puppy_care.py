puppy_food_kg = int(input())
command = input()

puppy_food_grams = puppy_food_kg * 1000
puppy_food_total = 0

while command != "Adopted":
    puppy_food_total += int(command)
    command = input()

if puppy_food_total <= puppy_food_grams:
    print(f"Food is enough! Leftovers: {puppy_food_grams - puppy_food_total} grams.")
elif puppy_food_total > puppy_food_grams:
    print(f"Food is not enough. You need {puppy_food_total - puppy_food_grams} grams more.")