from math import ceil
worker1_eff = int(input())
worker2_eff = int(input())
worker3_eff = int(input())
students_count = int(input())

total_worker_eff = worker1_eff + worker2_eff + worker3_eff
hours_counter = 0
difference = 0

if total_worker_eff == students_count:
    hours_counter += 1
elif total_worker_eff > students_count > 0:
    difference = ceil(total_worker_eff / students_count)
    for hour in range(1, difference+1):
        hours_counter += 1
        if hours_counter % 4 == 0:
            hours_counter += 1
elif total_worker_eff < students_count > 0:
    difference = ceil(students_count / total_worker_eff)
    for hour in range(1, difference+1):
        hours_counter += 1
        if hours_counter % 4 == 0:
            hours_counter += 1

print(f'Time needed: {hours_counter}h.')
