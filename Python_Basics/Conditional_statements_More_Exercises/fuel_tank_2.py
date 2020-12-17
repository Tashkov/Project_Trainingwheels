fuel = input()
liters = float(input())
club_card = input()

gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93

if club_card == 'Yes':
    """Price with discount"""
    card_discount_gasoline = gasoline_price - 0.18
    card_discount_diesel = diesel_price - 0.12
    card_discount_gas = gas_price - 0.08

    card_fuel_gasoline = card_discount_gasoline * liters
    card_fuel_diesel = card_discount_diesel * liters
    card_fuel_gas = card_discount_gas * liters

    if liters < 20:
        if fuel == "Gasoline":
            print(f"{card_fuel_gasoline:.2f} lv.")
        elif fuel == "Diesel":
            print(f'{card_fuel_diesel:.2f} lv.')
        elif fuel == "Gas":
            print(f'{card_fuel_gas * liters:.2f} lv.')
    elif liters == 20 or liters <= 25:
        discount_gasoline1 = card_fuel_gasoline * 0.08
        discount_diesel1 = card_fuel_diesel * 0.08
        discount_gas1 = card_fuel_gas * 0.08
        if fuel == "Gasoline":
            print(f"{card_fuel_gasoline - discount_gasoline1:.2f} lv.")
        elif fuel == "Diesel":
            print(f'{card_fuel_diesel - discount_diesel1:.2f} lv.')
        elif fuel == "Gas":
            print(f'{card_fuel_gas - discount_gas1:.2f} lv.')
    elif liters > 25:
        discount_gasoline1 = card_fuel_gasoline * 0.10
        discount_diesel1 = card_fuel_diesel * 0.10
        discount_gas1 = card_fuel_gas * 0.10
        if fuel == "Gasoline":
            print(f"{card_fuel_gasoline - discount_gasoline1:.2f} lv.")
        elif fuel == "Diesel":
            print(f'{card_fuel_diesel - discount_diesel1:.2f} lv.')
        elif fuel == "Gas":
            print(f'{card_fuel_gas - discount_gas1:.2f} lv.')
if club_card == "No":
    total_gasoline = gasoline_price * liters
    total_diesel = diesel_price * liters
    total_gas = gas_price * liters
    if liters < 20:
        if fuel == "Gasoline":
            print(f"{total_gasoline:.2f} lv.")
        elif fuel == "Diesel":
            print(f'{total_diesel:.2f} lv.')
        elif fuel == "Gas":
            print(f'{total_gas:.2f} lv.')
    elif liters == 20 or liters <= 25:
        discount_gasoline1 = total_gasoline * 0.08
        discount_diesel1 = total_diesel * 0.08
        discount_gas1 = total_gas * 0.08
        if fuel == "Gasoline":
            print(f"{total_gasoline - discount_gasoline1:.2f} lv.")
        elif fuel == "Diesel":
            print(f'{total_diesel - discount_diesel1:.2f} lv.')
        elif fuel == "Gas":
            print(f'{total_gas - discount_gas1:.2f} lv.')
    elif liters > 25:
        discount_gasoline2 = total_gasoline * 0.10
        discount_diesel2 = total_diesel * 0.10
        discount_gas2 = total_gas * 0.10
        if fuel == "Gasoline":
            print(f"{total_gasoline - discount_gasoline2:.2f} lv.")
        elif fuel == "Diesel":
            print(f'{total_diesel - discount_diesel2:.2f} lv.')
        elif fuel == "Gas":
            print(f'{total_gas - discount_gas2:.2f} lv.')