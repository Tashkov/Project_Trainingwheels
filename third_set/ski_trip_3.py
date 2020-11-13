days = int(input())
room = input()
rating = input()
one_person = 18
apartment = 25
president_apartment = 35
nights = days - 1

if days < 10:
    if room == "room for one person":
        total = nights * one_person
    elif room == "apartment":
        final_price = nights * apartment
        discount = final_price * 0.3
        total = final_price - discount
    elif room == "president apartment":
        final_price = nights * president_apartment
        discount = final_price * 0.1
        total = final_price - discount
elif days == 10 or days <= 15:
    if room == "room for one person":
        total = nights * one_person
    elif room == "apartment":
        final_price = nights * apartment
        discount = final_price * 0.35
        total = final_price - discount
    elif room == "president apartment":
        final_price = nights * president_apartment
        discount = final_price * 0.15
        total = final_price - discount
elif days > 15:
    if room == "room for one person":
        total = nights * one_person
    elif room == "apartment":
        final_price = nights * apartment
        discount = final_price * 0.50
        total = final_price - discount
    elif room == "president apartment":
        final_price = nights * president_apartment
        discount = final_price * 0.20
        total = final_price - discount
if rating == "positive":
    additional_discount = total * 0.25
    print(f"{(total + additional_discount):.2f}")
elif rating == "negative":
    additional_discount = total * 0.1
    print(f"{(total - additional_discount):.2f}")

