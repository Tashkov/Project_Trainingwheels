season = input()  # duration is 4 months! could be one of 4 seasons
km_month = float(input())

money = 0

if km_month <= 5000:
    if season == "Summer":
        money = km_month * 0.90
    elif season == "Winter":
        money = km_month * 1.05
    else:
        money = km_month * 0.75

elif 5000 < km_month <= 10000:
    if season == "Summer":
        money = km_month * 1.10
    elif season == "Winter":
        money = km_month * 1.25
    else:
        money = km_month * 0.95

elif 10000 < km_month <= 20000:
    money = km_month * 1.45

money *= 0.90 * 4
print(f"{money:.2f}")

