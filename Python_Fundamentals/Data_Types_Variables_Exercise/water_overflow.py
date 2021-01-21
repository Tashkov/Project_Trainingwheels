n = int(input())

capacity = 255
input_water = 0

for i in range(n):
    liters_water = int(input())

    if liters_water > capacity:
        print("Insufficient capacity!")
    else:
        capacity -= liters_water
        input_water += liters_water
        continue

print(input_water)

# Figure out the logic of the task ....
