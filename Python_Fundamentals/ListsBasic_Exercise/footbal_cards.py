card = input()
the_card_list = list(set(card.split()))
team_A_counter = 11
team_B_counter = 11

for i in the_card_list:
    if "A" in i:
        team_A_counter -= 1
    elif "B" in i:
        team_B_counter -= 1

if team_A_counter < 7 or team_B_counter < 7:
    print(f"Team A - {team_A_counter}; Team B - {team_B_counter}")
    print("Game was terminated")
    exit()
else:
    print(f"Team A - {team_A_counter}; Team B - {team_B_counter}")

# Make it work 100/100 now its 80/100