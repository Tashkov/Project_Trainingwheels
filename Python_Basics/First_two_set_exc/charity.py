days_total = int(input())
bakers_total = int(input())
cakes_total = int(input())
waffles_total = int(input())
pancakes_total = int(input())

cake_price_total = cakes_total*45
waffle_price_total = waffles_total*5.80
pancake_price_total = pancakes_total*3.20

daily_earnings = (cake_price_total+waffle_price_total+pancake_price_total
                  )*bakers_total
all_earnings = daily_earnings * days_total

price_spending = all_earnings / 8

total_earnings = all_earnings - price_spending

print(total_earnings)

