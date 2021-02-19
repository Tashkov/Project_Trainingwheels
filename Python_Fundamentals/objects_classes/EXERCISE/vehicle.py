class Vehicle:
    def __init__(self, type, model, price, owner=None):
        self.type = type
        self.model = model
        self.price = price
        self.owner = owner

    def buy(self, money, owner):
        if money >= self.price and self.owner == "None":
            self.owner = owner
            return print(f"Successfully bought a {self.type}. Change: {money - self.price:.2f}")
        if money < self.price:
            return print("Sorry, not enough money")
        if self.owner != "None":
            return print("Car already sold")

    def sell(self):
        if self.owner != "None":
            self.owner = "None"
        else:
            "Vehicle has no owner"

    def __repr__(self):
        if self.owner != "None":
            return f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"

vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
vehicle.buy(15000, "Peter")
vehicle.buy(35000, "George")
print(vehicle)
vehicle.sell()
print(vehicle)
