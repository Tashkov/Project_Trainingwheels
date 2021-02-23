neighborhood = list(map(lambda x: int(x), input().split("@")))
command = input()
cupid_is_at = 0

while not command == "Love!":
    list_of_commands = command.split()
    jump_length = int(list_of_commands[1])
# Checks the Cupid`s current position and readjusts it.
    if jump_length + cupid_is_at > (len(neighborhood) - 1):
        cupid_is_at = 0
    else:
        cupid_is_at += jump_length
# Checks if a house has had V-day or not
    if neighborhood[cupid_is_at] <= 0:
        print(f"Place {cupid_is_at} already had Valentine's day.")
    else:
        neighborhood[cupid_is_at] -= 2
        if neighborhood[cupid_is_at] <= 0:
            print(f"Place {cupid_is_at} has Valentine's day.")

    command = input()
# Checks the end result of the mission
failed_counter = 0
for place in neighborhood:
    if place > 0:
        failed_counter += 1
print(f"Cupid's last position was {cupid_is_at}.")
if not failed_counter == 0:
    print(f"Cupid has failed {failed_counter} places.")
else:
    print(f"Mission was successful")
