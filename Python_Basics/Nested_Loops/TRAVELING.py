destination = input()
saved_money = 0
needed_money = 0

while destination != "End":
    budget = float(input())
    needed_money += budget
    while saved_money < budget:
        money_input = float(input())
        saved_money += money_input
        if saved_money >= budget:
            print(f"Going to {destination}!")
            saved_money -= saved_money
            needed_money -= needed_money
            destination = input()
            break



