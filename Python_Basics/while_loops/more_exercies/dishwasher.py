number_of_bottles = int(input())
dirty_dishes = input()

total_detergent_ml = number_of_bottles * 750
detergent = total_detergent_ml
cycle_counter = 0   # every third cycle we load pans
dishes = 0
pans = 0
is_not_enough = False

while dirty_dishes != "End" or is_not_enough == False:
    cycle_counter += 1

    if cycle_counter % 3 == 0:
        detergent -= (int(dirty_dishes) * 15)
        pans += int(dirty_dishes)
    else:
        detergent -= (int(dirty_dishes) * 5)
        dishes += int(dirty_dishes)
    if detergent < 0:
        is_not_enough = True
        break
    else:
        dirty_dishes = input()
    if dirty_dishes == "End":
        is_not_enough = True

if detergent < 0:
    print(f"Not enough detergent, {abs(detergent)} "
          f"ml. more necessary!")
else:
    print("Detergent was enough!")
    print(f"{dishes} dishes and {pans} pots were washed.")
    print(f"Leftover detergent {detergent} ml.")