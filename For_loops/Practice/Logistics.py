n_cargo = int(input())
price = 0
sum_cargo = 0
bus = 0
truck = 0
train = 0

for i in range(n_cargo):
    weight = int(input())
    sum_cargo += weight
    if weight <= 3:
        bus += weight
    if weight >= 4 and weight <= 11:
        truck += weight
    if weight >= 12:
        train += weight
median_price = ((bus * 200) + (truck * 175) + (train * 120)) / sum_cargo
p_bus = (bus / sum_cargo) * 100
p_truck = (truck / sum_cargo) * 100
p_train = (train / sum_cargo) * 100

print(f"{median_price:.2f}\n{p_bus:.2f}%\n{p_truck:.2f}%\n{p_train:.2f}%")