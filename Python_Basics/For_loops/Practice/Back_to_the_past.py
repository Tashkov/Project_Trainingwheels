money = float(input())
year = int(input())
ivan_age = 17
money_spent = 0

for i in range (1800, year + 1):
    ivan_age += 1
    if i % 2 == 0:
        money_spent += 12000
    if i % 2 != 0:
        money_spent += 12000 + (ivan_age * 50)

if money >= money_spent:
    print(f'Yes! He will live a carefree life and will have {money - money_spent:.2f} dollars left.')
else:
    print(f'He will need {money_spent - money:.2f} dollars to survive.')
