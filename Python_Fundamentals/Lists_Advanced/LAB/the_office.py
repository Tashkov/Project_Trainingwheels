employee_happiness = list(map(lambda x: int(x), input().split()))
improvement_factor = int(input())

for i in range(len(employee_happiness)):
    employee_happiness[i] *= improvement_factor
average_happiness = sum(employee_happiness) // len(employee_happiness)
happy_employees = []
for value in employee_happiness:
    if value > average_happiness:
        happy_employees.append(value)

if len(happy_employees) >= (len(employee_happiness) // 2):
    print(f'Score: {len(happy_employees)}/{len(employee_happiness)}. Employees are happy!')
else:
    print(f'Score: {len(happy_employees)}/{len(employee_happiness)}. Employees are not happy!')

