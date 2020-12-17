km = int(input())
day = input()

taxi_initial_price = 0.70
bus_initial_price = 0.09
train_initial_price = 0.06

if day == "day":
    if km < 20:
        print(f'{taxi_initial_price + (km * 0.79):.2f}')
    elif 20 <= km < 100:
        taxi = (taxi_initial_price + (km * 0.79))
        bus = km * 0.09
        if taxi > bus:
            print(f'{bus:.2f}')
        else:
            print(f'{taxi:.2f}')
    elif km >= 100:
        taxi = km * 0.79
        bus = km * 0.09
        train = km * 0.06
        if taxi < bus and taxi < train:
            print(f'{taxi:.2f}')
        elif bus < train and bus < taxi:
            print(f'{bus:.2f}')
        else:
            print(f'{train:.2f}')
elif day == "night":
    if km < 20:
        print(f"{taxi_initial_price + (km * 0.9):.2f}")
    elif 20 <= km < 100:
        taxi = (taxi_initial_price + (km * 0.9))
        bus = km * 0.09
        if taxi > bus:
            print(f'{bus:.2f}')
        else:
            print(f'{taxi:.2f}')
    elif km >= 100:
        taxi = (taxi_initial_price + (km * 0.9))
        bus = km * 0.09
        train = (km * 0.06)
        if taxi < bus and taxi < train:
            print(f'{taxi:.2f}')
        elif bus < train and bus < taxi:
            print(f'{bus:.2f}')
        else:
            print(f'{train:.2f}')