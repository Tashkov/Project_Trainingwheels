months = int(input())
water = 20
net = 15
sum_electricity = 0

for i in range(1, months + 1):
    number = float(input())
    sum_electricity += number

sum_water = water * months
sum_net = net * months
others = sum_water + sum_net + sum_electricity + ((sum_water + sum_net + sum_electricity) * 0.2)
sum_total = sum_water + sum_net + sum_electricity + others

print(f"Electricity: {sum_electricity:.2f} lv\n"
      f"Water: {sum_water:.2f} lv\n"
      f"Internet: {sum_net:.2f} lv\n"
      f"Other: {others:.2f} lv\n"
      f"Average: {sum_total / months:.2f} lv")

