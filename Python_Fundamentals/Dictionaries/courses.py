line = input()
courses_data = {}

while not line == "end":
    course_name, student_name = line.split(" : ")
    if course_name not in courses_data:
        courses_data[course_name] = []
        courses_data[course_name].append(student_name)
    else:
        courses_data[course_name].append(student_name)
    line = input()

sorted_courses = dict(sorted(courses_data.items(), key=lambda kvp: len(kvp[1]), reverse=True))

for key, value in sorted_courses.items():
    print(f"{key}: {len(value)}")
    value = sorted(value)
    for name in value:
        print(f"-- {name}")
