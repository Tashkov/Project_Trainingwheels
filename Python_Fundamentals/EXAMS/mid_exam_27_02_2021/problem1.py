needed_experience = float(input())
battles_count = int(input())
total_experience = 0
counter_battles = 0
for battle in range(1, battles_count + 1):
    earned_experience = float(input())
    battles_count -= 1
    counter_battles += 1
    if battle % 3 == 0:
        bonus = earned_experience * 0.15
        earned_experience += bonus
    elif battle % 5 == 0:
        penalty = earned_experience * 0.1
        earned_experience -= penalty
    elif battle % 15 == 0:
        bonus = earned_experience * 0.05
        earned_experience += bonus
    total_experience += earned_experience

    if total_experience >= needed_experience:
        break

if total_experience >= needed_experience:
    print(f'Player successfully collected his needed experience for {counter_battles} battles.')
else:
    print(f'Player was not able to collect the needed experience, {needed_experience-total_experience:.2f} more needed.')