from math import ceil

employee_efficiency1 = int(input())
employee_efficiency2 = int(input())
employee_efficiency3 = int(input())
total_people = int(input())

hour_counter = 0
sum_of_efficiency = employee_efficiency1 + employee_efficiency2 + employee_efficiency3
total_time = ceil(total_people / sum_of_efficiency)

for hour in range(1, total_time):
    if hour % 3 == 0:
        hour_counter += 1


print(f"Time needed: {total_time + hour_counter}h.")


