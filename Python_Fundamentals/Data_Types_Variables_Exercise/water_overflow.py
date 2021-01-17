n = int(input())

capacity = 225
input_water = 0

for i in range(n):
    liters_water = int(input())
    input_water += liters_water
    if input_water > capacity:
        print("Insufficient capacity!")

print(input_water)

# Figure out the logic of the task ....
