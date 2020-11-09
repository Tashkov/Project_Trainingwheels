vacation_price = float(input())
puzzles = int(input())
talking_dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())

"""Underneath are the prices per item"""

puzzles_price = 2.60
talking_dolls_price = 3
teddy_bears_price = 4.10
minions_price = 8.20
trucks_price = 2
"""Underneath is the body of the program"""

total_orders = puzzles + talking_dolls + teddy_bears + minions + trucks
total_price = ((puzzles*puzzles_price) + (talking_dolls*talking_dolls_price) + (teddy_bears*teddy_bears_price) + (minions*minions_price) + (trucks*trucks_price))

if total_orders >= 50:
    discount = total_price * 0.25
    new_total_price = total_price - discount
    rent_with_discount = new_total_price * 0.10
    new_total_winnings = new_total_price - rent_with_discount
    if new_total_winnings >= vacation_price:
        print(f"Yes! {new_total_winnings - vacation_price:.2f} lv left.")
    else:
        print(f"Not enough money! {vacation_price-new_total_winnings:.2f} lv needed.")
else:
    rent = total_price * 0.1
    total_winnings = total_price - rent
    if total_winnings >= vacation_price:
        print(f"Yes! {total_winnings - vacation_price:.2f} lv left.")
    else:
        print(f"Not enough money {vacation_price - total_winnings:.2f} lv needed.")

