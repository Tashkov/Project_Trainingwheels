rooms = int(input())

counter = 0
need_chairs = False
for room in range(1, rooms + 1):
    command = input().split()
    chairs = command[0]
    taken_chairs = command[1]
    if len(chairs) >= int(taken_chairs):
        counter += len(chairs) - int(taken_chairs)
    else:
        need_chairs = True
        needed_charis = int(taken_chairs) - len(chairs)
        print(f'{needed_charis} more chairs needed in room {room}')
if not need_chairs:
    print(f'Game On, {counter} free chairs left')
