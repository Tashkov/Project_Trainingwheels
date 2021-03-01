initial_energy = int(input())
command = input()
won_battles = 0

while not command == "End of battle":
    distance = int(command)
    if distance > initial_energy:
        print(f"Not enough energy! Game ends with {won_battles} won battles and {initial_energy} energy")
        exit()
    initial_energy -= distance
    won_battles += 1
    if won_battles % 3 == 0:
        initial_energy += won_battles

    command = input()

if command == "End of battle" and initial_energy >= 0:
    print(f"Won battles: {won_battles}. Energy left: {initial_energy}")
else:
    print(f"Won battles: {won_battles}. Energy left: {initial_energy}")
