line = input()
users_points = {}
exams_counts = {}

while not line == "exam finished":
    token = line.split("-")
    username = token[0]
    command = token[1]
    if not command == "banned":
        language = command
        points = int(token[2])
        if username not in users_points:
            users_points[username] = points
        else:
            if points > users_points[username]:
                users_points[username] = points
        if language not in exams_counts:
            exams_counts[language] = 1
        else:
            exams_counts[language] += 1
    else:
        users_points.pop(username)

    line = input()

sorted_users = dict(sorted(users_points.items(), key=lambda kvp: (-kvp[1],kvp[0])))
sorted_languages = dict(sorted(exams_counts.items(), key=lambda kvp: (-kvp[1], kvp[0])))

print("Results:")
for key, value in sorted_users.items():
    print(f"{key} | {value}")
print("Submissions:")
for key, value in sorted_languages.items():
    print(f"{key} - {value}")
