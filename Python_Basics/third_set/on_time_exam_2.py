start_h = int(input())
start_m = int(input())
arrival_h = int(input())
arrival_m = int(input())

start_total_m = (start_h * 60) + start_m
arrival_total_m = (arrival_h * 60) + arrival_m
early = start_total_m - arrival_total_m
late = arrival_total_m - start_total_m
hour = late // 60
min = late % 60
hour_early = (early // 60) * -1
min_early = (early % 60)

if late > 0:
     if late <= 59:
        print(f'Late\n{late} minutes after the start')
     else:
        print(f"Late\n{hour}:{min:02d} hours after the start")
elif 0 <= early <= 30:
    if early != 0:
        print(f"On time\n{early} minutes before the start")
    elif early == 0:
        print("On time")
elif early > 30:
    if early <= 59:
        print(f"Early\n{early} minutes before the start")
    else:
        print(f"Early\n{hour_early * -1}:{min_early:02d} hours before the start")