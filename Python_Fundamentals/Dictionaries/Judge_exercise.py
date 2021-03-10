line = input()
contests_DB = {}
users_statistics = {}

while not line == "no more time":
    username, contest, points = line.split(" -> ")
    points = int(points)
    # works with the contest_DB dict
    if contest not in contests_DB:
        contests_DB[contest] = {}
        if username not in contests_DB[contest]:
            contests_DB[contest][username] = points
        else:
            if contests_DB[contest][username] < points:
                contests_DB[contest][username] = points
    else:
        if username not in contests_DB[contest]:
            contests_DB[contest][username] = points
        else:
            if contests_DB[contest][username] < points:
                contests_DB[contest][username] = points

    line = input()

# works with the users_statistics_DB
for course in contests_DB.keys():
    for participant, result in contests_DB[course].items():
        if participant not in users_statistics:
            users_statistics[participant] = result
        else:
            users_statistics[participant] += result

sorted_users_stats = dict(sorted(users_statistics.items(), key=lambda kvp: -kvp[1]))
# Sorts the nested dictionaries first by points descending then by name alphabetically
for each_contest in contests_DB.keys():
    contests_DB[each_contest] = dict(sorted(contests_DB[each_contest].items(), key=lambda kvp: (-kvp[1], kvp[0])))

counter_courses = 0
for key in contests_DB.keys():
    counter_courses = 0
    print(f"{key}: {len(contests_DB[key])} participants")
    for user, points in contests_DB[key].items():
        counter_courses += 1
        print(f"{counter_courses}. {user} <::> {points}")
counter_individual_performance = 0
print(f"Individual standings:")
for participant, final_score in sorted_users_stats.items():
    counter_individual_performance += 1
    print(f"{counter_individual_performance}. {participant} -> {final_score}")
