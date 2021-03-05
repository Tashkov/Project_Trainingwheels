n_commands = int(input())
entries_dict = {}

for person in range(1, n_commands + 1):
    line = input()
    token = line.split()
    command = token[0]
    if command == "register":
        username = token[1]
        license_num = token[2]
        if username not in entries_dict:
            entries_dict[username] = license_num
            print(f"{username} registered {license_num} successfully")
        else:
            print(f'ERROR: already registered with plate number {entries_dict[username]}')
    elif command == "unregister":
        username = token[1]
        if username not in entries_dict:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            entries_dict.pop(username)

for key, value in entries_dict.items():
    print(f"{key} => {value}")