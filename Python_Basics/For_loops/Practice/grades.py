n_students = int(input())
sum_students = 0
sum_grades = 0
fail = 0
three_four = 0
four_five = 0
top_students = 0

for i in range(n_students):
    grade = float(input())
    sum_students += 1
    sum_grades += grade
    if grade < 3:
        fail += 1
    if grade >= 3 and grade <= 3.99:
        three_four += 1
    if grade >= 4 and grade <= 4.99:
        four_five += 1
    if grade >= 5:
        top_students += 1

average_grade = sum_grades / sum_students
p_top = top_students / sum_students * 100
p_four_five = four_five / sum_students * 100
p_three_four = three_four / sum_students * 100
p_fail = fail / sum_students * 100

print(f"Top students: {p_top:.2f}%\nBetween 4.00 and 4.99: {p_four_five:.2f}%\n"
      f"Between 3.00 and 3.99: {p_three_four:.2f}%\nFail: {p_fail:.2f}%\nAverage: {average_grade:.2f}")