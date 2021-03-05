def average_grade(students: dict):
    for key, value in students.items():
        delimeter = len(value)
        sum_grades = sum(value)
        students[key] = sum_grades / delimeter

    return students



row_pairs = int(input())
academy_book = {}

for entry in range(1, row_pairs + 1):
    name = input()
    grade = float(input())
    if name not in academy_book:
        academy_book[name] = []
        academy_book[name].append(grade)
    else:
        academy_book[name].append(grade)

average_grade(academy_book)
working_dictionary = academy_book.copy()

for key, value in academy_book.items():
    if value < 4.50:
        working_dictionary.pop(key)

sorted_academy_book = dict(sorted(working_dictionary.items(), key=lambda kvp: kvp[1], reverse=True))

for key, value in sorted_academy_book.items():
    print(f"{key} -> {value:.2f}")