from math import ceil
student_attendances = int(input())
course_lectures = int(input())
initial_bonus = int(input())

students_attendance_list = []
total_bonus = 0
best_student = 0

if course_lectures > 0 and student_attendances > 0:
    for i in range(1, student_attendances + 1):
        attendance_per_student = int(input())
        students_attendance_list.append(attendance_per_student)
    best_student = max(students_attendance_list)
    total_bonus = ceil((best_student / course_lectures) * (5 + initial_bonus))


print(f'Max Bonus: {total_bonus}.')
print(f'The student has attended {best_student} lectures.')
