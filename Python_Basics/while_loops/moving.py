width = int(input())
lenght = int(input())
height = int(input())
inpt = input()
room = width * lenght * height
box_sum = 0

while inpt != "Done":
    box = int(inpt)
    box_sum += box
    if room < box_sum:
        print(f"No more free space! You need {box_sum - room} Cubic meters more.")
        break
    inpt = input()
if box_sum <= room:
    print(f"{room - box_sum} Cubic meters left.")