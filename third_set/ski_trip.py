days = int(input())
room = input()
rate = input()
single_room = 18
double_room = 25
apartment = 35

if rate == "positive":
    if room == "room for one person":
        print(f"{(((days-1) * single_room) - (((days-1) * single_room) * 0.25)):.2f}")
    elif room == "apartment":
        if days < 10:
            print(f"{(((days-1)*double_room) - (((days-1)*double_room) * 0.3)) * 0.25:.2f}")
        elif days == 10 or days <= 15:
            print(f"{(((days-1)*double_room) - (((days-1)*double_room) * 0.35)) * 0.25:.2f}")
        elif days > 15:
            print(f"{(((days-1)*double_room) - (((days-1)*double_room) * 0.5)) * 0.25:.2f}")
    elif room == "president apartment":
        if days < 10:
            print(f"{(((days-1) * apartment) - (((days-1) * apartment) * 0.1)) * 0.25:.2f}")
        elif days == 10 or days <= 15:
            print(f"{(((days-1) * apartment) - (((days-1) * apartment) * 0.15)) * 0.25:.2f}")
        elif days > 15:
            print(f"{(((days-1) * apartment) - (((days-1) * apartment) * 0.2)) * 0.25:.2f}")
elif rate == "negative":
    if room == "room for one person":
        print(f"{(((days-1) * single_room) - (((days-1) * single_room) * 0.1)):.2f}")
    elif room == "apartment":
        if days < 10:
            print(f"{(((days-1) * double_room) - (((days-1) * double_room) * 0.3)) * 0.1:.2f}")
        elif days == 10 or days <= 15:
            print(f"{(((days-1) * double_room) - (((days-1) * double_room) * 0.35)) * 0.1:.2f}")
        elif days > 15:
            print(f"{(((days-1) * double_room) - (((days-1) * double_room) * 0.5)) * 0.1:.2f}")
    elif room == "president apartment":
        if days < 10:
            print(f"{(((days-1) * apartment) - (((days-1) * apartment) * 0.1)) * 0.1:.2f}")
        elif days == 10 or days <= 15:
            print(f"{(((days-1) * apartment) - (((days-1) * apartment) * 0.15)) * 0.1:.2f}")
        elif days > 15:
            print(f"{(((days-1) * apartment) - (((days-1) * apartment) * 0.2)) * 0.1:.2f}")