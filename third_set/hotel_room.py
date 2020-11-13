month = input()
stay = int(input())

price1 = 0
price2 = 0
"""price1 is studio  
price2 is apartment """

if month == "May" or month == "October":
    price1 = 50
    price2 = 65
    if stay > 14:
        discount = price1 * 0.3
        price1 -= discount
    elif stay > 7:
        discount = price1 * 0.05
        price1 -= discount

elif month == "June" or month == "September":
    price1 = 75.20
    price2 = 68.70
    if stay > 14:
        discount = price1 * 0.2
        price1 -= discount
elif month == "July" or month == "August":
    price1 = 76
    price2 = 77

if stay > 14:
    discount = price2 * 0.1
    price2 -= discount

sum_total_price1 = price1 * stay
sum_total_price2 = price2 * stay
print(f"Apartment: {sum_total_price2:.2f} lv.\nStudio: {sum_total_price1:.2f} lv.")
