plunder_days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
total_plunder = 0

for day in range(1, plunder_days + 1):
    total_plunder += daily_plunder
    if day % 3 == 0:
        total_plunder += daily_plunder * 0.5
    elif day % 5 == 0:
        total_plunder -= total_plunder * 0.3


if total_plunder >= expected_plunder:
    print(f'Ahoy! {total_plunder:.2f} plunder gained.')
elif total_plunder < expected_plunder:
    if total_plunder == 0:
        exit()
    else:
        percentage = (total_plunder / expected_plunder) * 100
        print(f'Collected only {percentage:.2f}% of the plunder.')
