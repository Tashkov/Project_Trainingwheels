def the_best_result_is(best_dict: dict):
    previous_value = 0
    ace_user = ""
    for k, v in best_dict.items():
        if previous_value < v:
            previous_value = v
            ace_user = k
    return previous_value, ace_user

def sorting_the_contests(user_contests_DB: dict):
    for key, value in user_contests_DB.items():
        user_contests_DB[key] = dict(sorted(value.items(), key=lambda kvp: kvp[1], reverse=True))
    return user_contests_DB


line = input()
contests_DB = {}
user_results_DB = {}
while not line == "end of contests":
    token = line.split(":")
    contest_name = token[0]
    contest_password = token[1]
    contests_DB[contest_name] = contest_password

    line = input()

line2 = input()
while not line2 == "end of submissions":
    name_contest, password, username, points = line2.split("=>")
    points = int(points)
    if name_contest in contests_DB and contests_DB[name_contest] == password:
        if username not in user_results_DB:
            user_results_DB[username] = {}
            if name_contest not in user_results_DB[username]:
                user_results_DB[username][name_contest] = points
            else:
                if user_results_DB[username][name_contest] < points:
                    user_results_DB[username][name_contest] = points
        else:
            if name_contest not in user_results_DB[username]:
                user_results_DB[username][name_contest] = points
            else:
                if user_results_DB[username][name_contest] < points:
                    user_results_DB[username][name_contest] = points
    line2 = input()
best_result = {}

for key in user_results_DB.keys():
    sum_points = 0
    for value in user_results_DB[key].values():
        sum_points += int(value)
        best_result[key] = sum_points

ace_result, ace_user = the_best_result_is(best_result)
print(f"Best candidate is {ace_user} with total {ace_result} points.")
print("Ranking:")

sorted_user_results = dict(sorted(user_results_DB.items()))
sorting_the_contests(sorted_user_results)

for user in sorted_user_results.keys():
    print(f"{user}")
    for contest, points in sorted_user_results[user].items():
        print(f"#  {contest} -> {points}")
