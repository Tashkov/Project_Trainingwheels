first_line = int(input())
money = input()

expected_income = 0
card_payment = 0
card_counter = 0
cash_payment = 0
cash_counter = 0
counter = 0
money_is_enough = False

while money != "End" or money_is_enough == False:
    counter += 1
    if counter % 2 == 0:
        if int(money) < 10:
            print("Error in transaction!")
        else:
            card_counter += 1
            card_payment += float(money)
            expected_income += float(money)
            print("Product sold!")
    elif counter % 2 != 0:
        if int(money) > 100:
            print("Error in transaction!")
        else:
            cash_counter += 1
            cash_payment += float(money)
            expected_income += float(money)
            print("Product sold!")
    if expected_income >= first_line:
        money_is_enough = True
        break
    else:
        money = input()
    if money == "End":
        money_is_enough = True

if money == "End":
    print("Failed to collect required money for charity.")
else:
    if expected_income >= first_line:
        print(f"Average CS: {cash_payment / cash_counter:.2f}\n"
              f"Average CC: {card_payment / card_counter:.2f}")
