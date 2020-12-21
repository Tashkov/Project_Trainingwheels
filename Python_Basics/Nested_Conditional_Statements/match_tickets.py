budget = float(input())
ticket_type = input()  # could be VIP or Normal predefined in variables
people_going = int(input())

money_for_transport = 0
ticket_price = 0
total_tickets = 0
net_budget = 0

if ticket_type == "VIP":
    ticket_price = 499.99
    if 1 <= people_going <= 4:
        money_for_transport = budget * 0.75
    elif 5 <= people_going <= 9:
        money_for_transport = budget * 0.60
    elif 10 <= people_going <= 24:
        money_for_transport = budget * 0.50
    elif 25 <= people_going <= 49:
        money_for_transport = budget * 0.40
    elif people_going >= 50:
        money_for_transport = budget * 0.25

elif ticket_type == "Normal":
    ticket_price = 249.99
    if 1 <= people_going <= 4:
        money_for_transport = budget * 0.75
    elif 5 <= people_going <= 9:
        money_for_transport = budget * 0.60
    elif 10 <= people_going <= 24:
        money_for_transport = budget * 0.50
    elif 25 <= people_going <= 49:
        money_for_transport = budget * 0.40
    elif people_going >= 50:
        money_for_transport = budget * 0.25

total_tickets = ticket_price * people_going
net_budget = budget - money_for_transport

if total_tickets <= net_budget:
    print(f"Yes! You have {net_budget - total_tickets:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(net_budget - total_tickets):.2f} leva.")
