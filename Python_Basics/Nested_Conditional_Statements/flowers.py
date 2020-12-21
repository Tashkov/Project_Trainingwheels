flower1 = int(input())  # int btw 0 ... 200
flower2 = int(input())  # int btw 0 ... 200
flower3 = int(input())  # int btw 0 ... 200
season = input()  # Could be Spring, Summer, Autumn or Winter
is_holiday = input()  # Could be Y or N

total_flowers = flower1 + flower2 + flower3
flower1_money = 0
flower2_money = 0
flower3_money = 0
bouquet = 0

if season == "Spring" or season == "Summer":
    flower1_money = flower1 * 2
    flower2_money = flower2 * 4.10
    flower3_money = flower3 * 2.50
    bouquet = flower1_money + flower2_money + flower3_money
    if is_holiday == "Y":
        bouquet += bouquet * 0.15
    if season == "Spring" and flower3 > 7:
        bouquet -= bouquet * 0.05

elif season == "Autumn" or season == "Winter":
    flower1_money = flower1 * 3.75
    flower2_money = flower2 * 4.50
    flower3_money = flower3 * 4.15
    bouquet = flower1_money + flower2_money + flower3_money
    if is_holiday == "Y":
        bouquet += bouquet * 0.15
    if season == "Winter" and flower2 >= 10:
        bouquet -= bouquet * 0.10

if total_flowers > 20:
    bouquet -= bouquet * 0.20
print(f"{(bouquet + 2):.2f}")

