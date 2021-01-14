quantity = int(input())
days = int(input())

ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15
budget = 0
spirit = 0

for i in range(1, days + 1):
    if i % 2 == 0:
        budget += ornament_set * quantity
        spirit += 5
    if i % 3 == 0:
        budget += (tree_skirt + tree_garland) * quantity
        spirit += 13
    if i % 5 == 0:
        budget += tree_lights * quantity
        if i % 3 == 0:
            spirit += 47
        else:
            spirit += 17
    if i % 10 == 0:
        spirit -= 20
        budget += (tree_skirt + tree_garland + tree_lights) * 1
        if i == days:
            spirit -= 30
    if i % 11 == 0:
        quantity += 2

print(f"Total cost: {budget}\nTotal spirit: {spirit}")
