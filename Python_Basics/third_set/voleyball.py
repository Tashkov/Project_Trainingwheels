from math import floor

year = input()
holidays = int(input())
weekends_home = int(input())

weekends_Sofia = 48 - weekends_home
weekends_Sofia_not_working = (weekends_Sofia * 3) / 4
holidays_Sofia = (holidays * 2) / 3
total_games = weekends_Sofia_not_working + holidays_Sofia + weekends_home

print(weekends_Sofia, weekends_Sofia_not_working, holidays_Sofia, total_games)

if year == "leap":
    bonus = total_games * 0.15
    total_games = floor(total_games + bonus)
    print(total_games)
else:
    print(floor(total_games))
