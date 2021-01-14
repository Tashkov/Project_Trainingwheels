days_total = int(input())  # btw 1 - 5
hours_total = int(input())  # btw 1 - 24

fee = 0
days_counter = 0
total_money = 0
daily_money = 0

for day in range(1, days_total + 1):
    for hour in range(1, hours_total + 1):
        if day % 2 == 0 and hour % 2 != 0:
            fee = 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            fee = 1.25
        else:
            fee = 1
        daily_money += fee
    total_money += daily_money
    days_counter += 1
    print(f"Day: {days_counter} - {daily_money:.2f} leva")
    daily_money = 0
print(f"Total: {total_money:.2f} leva")
