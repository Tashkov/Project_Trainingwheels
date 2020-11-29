money_needed = float(input())
money_balance = float(input())
days = 0

while True:
    action = input()
    money = float(input())
    if action == "spend":
        days += 1
        if money <= money_balance:
            money_balance -= money
        elif money > money_balance:
            money_balance = 0
        if days == 5:
            print(f"You can't save the money.\n{days}")
            break
    elif action == "save":
        days += 1
        money_balance += money
    if money_balance >= money_needed:
        print(f"You saved the money for {days} days.")
        break
