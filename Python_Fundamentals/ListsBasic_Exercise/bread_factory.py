activities = input().split("|")

energy = 100
coins = 100

for activity in activities:
    action_ingredient = activity.split("-")
    event_ingredient = action_ingredient[0]
    amount = action_ingredient[1]
    if event_ingredient == "rest" and energy > 100 and not (amount + energy) > 100:
        energy += amount
    else:
        print(f'Current energy: {energy}.')
    if event_ingredient == "order" and energy >= 30:
        energy -= 30
        print(f'You earned {amount} coins.')

