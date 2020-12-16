age = int(input())
price_washing_machine = float(input())
toy_price = int(input())
years = []
birthday_cash = []
sum_cash = 10
brother_steals = 0

for i in range(age):
    age -= 1
    birthdays = years.append(age)

#lists of numbers of years
toys = years[0::2]
cash = years[1::2]

sum_toys_cash = (len(toys)) * toy_price

for i in cash:
    birthday_cash.append(sum_cash)
    sum_cash += 10
    brother_steals += 1
total_birthday_cash = (sum(birthday_cash)) - brother_steals
net_total_money = total_birthday_cash + sum_toys_cash

if price_washing_machine <= net_total_money:
    print(f'Yes! {net_total_money - price_washing_machine:.2f}')
elif price_washing_machine > net_total_money:
    print(f'No! {price_washing_machine - net_total_money:.2f}')

#Make it more pythonic