initial_dungeon = input().split("|")
health = 100
bitcoins = 0
counter = 0

for room in initial_dungeon:
    dungeon = room.split()
    action = dungeon[0]
    value = int(dungeon[1])

    if action == "potion":
        counter += 1
        health += value
        if health > 100:
            print(f'You healed for {value - (health - 100)} hp.')
            health = 100
            print(f'Current health: {health} hp.')
        else:
            print(f'You healed for {value} hp.')
            print(f'Current health: {health} hp.')
    elif action == "chest":
        counter += 1
        bitcoins += value
        print(f'You found {value} bitcoins.')
    else:
        if not health <= 0:
            counter += 1
            health -= value
            if health <= 0:
                print(f'You died! Killed by {action}.')
                print(f'Best room: {counter}')
                exit()
            else:
                print(f'You slayed {action}.')
        else:
            print(f'You died! Killed by {action}.')
            print(f'Best room: {counter}')
            exit()

if counter == len(initial_dungeon):
    print("You've made it!")
    print(f'Bitcoins: {bitcoins}')
    print(f'Health: {health}')