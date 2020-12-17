from math import floor, ceil

flower_m = int(input())
flower_z = int(input())
flower_r = int(input())
flower_c = int(input())
gift_price = float(input())

flowers_price = (flower_m * 3.25) + (flower_z * 4) + (flower_r * 3.50) +(flower_c * 8)
tax = flowers_price * 0.05
total_price = flowers_price - tax

if total_price >= gift_price:
    money_left = floor(total_price - gift_price)
    print(f'She is left with {money_left} leva.')
else:
    money_needed = ceil(gift_price - total_price)
    print(f'She will have to borrow {money_needed} leva.')