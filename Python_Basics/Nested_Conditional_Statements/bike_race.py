junior_bikers = int(input())
senior_bikers = int(input())
track_type = input()  # could be one of 3: "trail", "cross-country", "downhill", "road"

total_bikers = junior_bikers + senior_bikers
junior_money = 0
senior_money = 0
total_money = 0

if track_type == "trail":
    junior_money = 5.50 * junior_bikers
    senior_money = 7 * senior_bikers
elif track_type == "cross-country":
    if total_bikers >= 50:
        junior_money = (8 - (8 * 0.25)) * junior_bikers
        senior_money = (9.50 - (9.50 * 0.25)) * senior_bikers
    else:
        junior_money = 8 * junior_bikers
        senior_money = 9.50 * senior_bikers
elif track_type == "downhill":
    junior_money = 12.25 * junior_bikers
    senior_money = 13.75 * senior_bikers
elif track_type == "road":
    junior_money = 20 * junior_bikers
    senior_money = 21.50 * senior_bikers

total_money = junior_money + senior_money
discount = total_money * 0.05
donated_money = total_money - discount

print(f"{donated_money:.2f}")


