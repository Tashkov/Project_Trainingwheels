from math import floor

hours = int(input())
days = int(input())
employees = int(input())

study_days = days * 0.1
overtime = employees * (2 * days)
work_hours = floor((days - study_days) * 8) + overtime

if work_hours >= hours:
    time_left = floor(work_hours - hours)
    print(f"Yes!{time_left} hours left.")
else:
    time_needed = floor(hours - work_hours)
    print(f"Not enough time!{time_needed} hours needed.")
