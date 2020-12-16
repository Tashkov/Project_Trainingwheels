fail_threshold = int(input())

solved_problems = 0
failed_tasks = 0
grades_total = 0
last_task = ""


while failed_tasks < fail_threshold:
    task_name = input()
    if task_name == "Enough":
        break

    grade = int(input())
    if grade <= 4:
        failed_tasks += 1
    grades_total += grade
    solved_problems += 1
    last_task = task_name

if failed_tasks == fail_threshold:
    print(f"You need a break, {fail_threshold} poor grades.")
else:
    print(f'Average score: {grades_total / solved_problems:.2f}\n'
          f'Number of problems: {solved_problems}\n'
          f'Last problem: {last_task}')
