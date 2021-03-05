line = input()
users_sides = {}
dark_users = {}

while not line == "Lumpawaroo":
    line2 = line.split()
    if "|" in line2:
        token = line.split(" | ")
        force_side = token[0]
        force_user = token[1]
        if force_side not in users_sides:
            users_sides[force_side] = []
            if force_user not in users_sides[force_side]:
                users_sides[force_side].append(force_user)
        else:
            if force_user not in users_sides[force_side]:
                users_sides[force_side].append(force_user)

    elif "->" in line2:
        token = line.split(" -> ")
        force_side = token[1]
        force_user = token[0]
        list_of_keys = [key for key in users_sides.keys()]
        key1 = list_of_keys[0]
        key2 = list_of_keys[1]
        if force_user in users_sides[key1]:
            users_sides[key1].remove(force_user)
            users_sides[key2].append(force_user)
            print(f"{force_user} joins the {force_side} side!")

        elif force_user in users_sides[key2]:
            users_sides[key2].remove(force_user)
            users_sides[key1].append(force_user)
            print(f"{force_user} joins the {force_side} side!")
        else:
            users_sides[force_side].append(force_user)
            print(f"{force_user} joins the {force_side} side!")

    line = input()

sorted_users = dict(sorted(users_sides.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))

for key in sorted_users.keys():
    if len(sorted_users[key]) != 0:
        print(f"Side: {key}, Members: {len(sorted_users[key])}")
        sorted_list_users = sorted(sorted_users[key])
        for user in sorted_list_users:
            print(f"! {user}")
