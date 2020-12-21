budget = float(input())
season = input()  # Summer or Winter

type_class = ""
type_car = ""
car_price = 0

if budget <= 100:  # Economy class
    type_class = "Economy class"
    if season == "Summer":
        type_car = "Cabrio"
        car_price = budget * 0.35
    elif season == "Winter":
        type_car = "Jeep"
        car_price = budget * 0.65
elif 100 < budget <= 500:
    type_class = "Compact class "
    if season == "Summer":
        type_car = "Cabrio"
        car_price = budget * 0.45
    elif season == "Winter":
        type_car = "Jeep"
        car_price = budget * 0.80
elif budget > 500:
    type_class = "Luxury class"
    type_car = "Jeep"
    car_price = budget * 0.90

print(f"{type_class}\n"
      f"{type_car} - {car_price:.2f}")

