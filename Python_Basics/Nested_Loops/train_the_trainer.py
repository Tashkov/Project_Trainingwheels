number_of_people = int(input())
line = input()

sum_of_marks = 0
sum_of_all_marks = 0
mark_counter = 0

while line != "Finish":

    for marks in range(1, number_of_people + 1):
        mark = float(input())
        mark_counter += 1
        sum_of_all_marks += mark
        sum_of_marks += mark

    print(f"{line} - {(sum_of_marks / marks):.2f}.")

    sum_of_marks = 0

    line = input()
print(f"Student's final assessment is {(sum_of_all_marks / mark_counter):.2f}.")
