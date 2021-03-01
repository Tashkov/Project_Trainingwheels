total_people = int(input())
lift = [int(x) for x in input().split()]

if total_people != 0:
    for index, wagon in enumerate(lift):
        reference_total_people = total_people
        if 0 <= wagon < 4:
            seats_left = 4 - wagon
            if seats_left > total_people:
                lift[index] += total_people
                total_people -= total_people
            else:
                total_people -= seats_left
                if lift[index] == 0:
                    lift[index] += reference_total_people - total_people
                else:
                    lift[index] += seats_left


if total_people == 0 and sum(lift) != len(lift) * 4:
    print(f"The lift has empty spots!")
    print(*lift, sep=" ")
elif total_people > 0 and sum(lift) == len(lift) * 4:
    print(f"There isn't enough space! {total_people} people in a queue!")
    print(*lift, sep=" ")
elif total_people == 0 and sum(lift) == len(lift) * 4:
    print(*lift, sep=" ")