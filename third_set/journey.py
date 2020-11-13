budget = float(input())
season = input()

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        place = "Camp"
        money_spent = budget * 0.3
        print(f"Somewhere in Bulgaria\n{place} - {money_spent:.2f}")
    elif season == 'winter':
        place = "Hotel"
        money_spent = budget * 0.7
        print(f"Somewhere in Bulgaria\n{place} - {money_spent:.2f}")
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        place = "Camp"
        money_spent = budget * 0.4
        print(f"Somewhere in Balkans\n{place} - {money_spent:.2f}")
    elif season == "winter":
        place = "Hotel"
        money_spent = budget * 0.8
        print(f"Somewhere in Balkans\n{place} - {money_spent:.2f}")
elif budget > 1000:
    destination = "Europe"
    money_spent = budget * 0.9
    place = "Hotel"
    print(f"Somewhere in Europe\n{place} - {money_spent:.2f}")
