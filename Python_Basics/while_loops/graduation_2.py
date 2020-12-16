name = input()
yearly_mark = 0.0
marks_sum = 0.0
grade = 1.0
excluded = 0

while grade < 13:
    mark = float(input())
    if mark < 4.0:
        excluded += 1
        if excluded > 1:
            print(f'{name} has been excluded at {int(grade)} grade')
            break
        continue
    grade += 1
    marks_sum += mark
if grade == 13:
    average = marks_sum / 12
    print(f'{name} graduated. Average grade: {average:.2f}')
