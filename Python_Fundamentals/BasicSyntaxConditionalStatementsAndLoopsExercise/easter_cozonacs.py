budget = float(input())
flour_price_per_kg = float(input())

eggs_price = flour_price_per_kg * 0.75
milk_price = (flour_price_per_kg + (flour_price_per_kg * 0.25)) * 0.250
counter_cozonacs = 0
counter_eggs = 0
one_cozonak = flour_price_per_kg + eggs_price + milk_price

while budget > one_cozonak:
    budget -= one_cozonak
    counter_eggs += 3
    counter_cozonacs += 1
    if counter_cozonacs % 3 == 0:
        counter_eggs -= (counter_cozonacs - 2)
print(f"You made {counter_cozonacs} cozonacs! Now you have {counter_eggs} eggs and {budget:.2f}BGN left.")