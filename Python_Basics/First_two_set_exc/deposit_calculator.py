money = float(input())
time = int(input())
glp = float(input())
lihva_year = (money * glp) / 100
lihva_month = lihva_year/12
earnings = lihva_month * time


money_sum = money + earnings

print(money_sum)
