gas = input()
liters = float(input())

if liters >= 25.00 and (gas == "Diesel" or gas == "Gasoline" or gas == "Gas"):
    print(f"You have enough {gas.lower()}.")
elif liters < 25.00 and (gas == "Diesel" or gas == "Gasoline" or gas == "Gas"):
    print(f'Fill your tank with {gas.lower()}!')
else:
    print(f"Invalid fuel!")
