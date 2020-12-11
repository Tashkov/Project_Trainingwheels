floors = int(input())
rooms = int(input())

for i in range(floors, 0, -1):
    print()
    for n in range(0, rooms):
        if i == floors:
            print(f"L{i}{n}", end=" ")
        elif i % 2 == 0:
            print(f"O{i}{n}", end=" ")
        elif i % 2 != 0:
            print(f"A{i}{n}", end=" ")

