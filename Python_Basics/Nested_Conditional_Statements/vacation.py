budget = float(input())
season = input()  # Could be Summer or Winter

accommodation = ""
location = ""
money = 0

if budget <= 1000:
    accommodation = "Camp"
    if season == "Summer":
        location = "Alaska"
        money = budget * 0.65
    elif season == "Winter":
        location = "Morocco"
        money = budget * 0.45

elif 1000 < budget <= 3000:
    accommodation = "Hut"
    if season == "Summer":
        location = "Alaska"
        money = budget * 0.80
    elif season == "Winter":
        location = "Morocco"
        money = budget * 0.60
elif budget > 3000:
    accommodation = "Hotel"
    money = budget * 0.90
    if season == "Summer":
        location = "Alaska"
    elif season == "Winter":
        location = "Morocco"

print(f"{location} - {accommodation} - {money:.2f}")