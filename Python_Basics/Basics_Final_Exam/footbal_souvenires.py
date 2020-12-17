team_name = input()

flags = 0
caps = 0
posters = 0
stickers = 0

if team_name == "Argentina" or team_name == "Brazil" or team_name == "Croatia" or team_name == "Denmark":
    gift_type = input()
    if gift_type == "flags" or gift_type == "caps" or gift_type == "posters" or gift_type == "stickers":
        gift_quantity = int(input())
        if team_name == "Argentina":
            if gift_type == "flags":
                total_money = gift_quantity * 3.25
                print(f"Pepi bought {gift_quantity} {gift_type} of {team_name} for {total_money:.2f} lv.")
            elif gift_type == "caps":
                total_money = gift_quantity * 7.20
                print(f"Pepi bought {gift_quantity} {gift_type} of {team_name} for {total_money:.2f} lv.")
            elif gift_type == "posters":
                total_money = gift_quantity * 5.10
                print(f"Pepi bought {gift_quantity} {gift_type} of {team_name} for {total_money:.2f} lv.")
            elif gift_type == "stickers":
                total_money = gift_quantity * 1.25
                print(f"Pepi bought {gift_quantity} {gift_type} of {team_name} for {total_money:.2f} lv.")
        elif team_name == "Brazil":
            if gift_type == "flags":
                total_money = gift_quantity * 4.20
                print(f"Pepi bought {gift_quantity} {gift_type} of {team_name} for {total_money:.2f} lv.")
            elif gift_type == "caps":
                total_money = gift_quantity * 8.50
                print(f"Pepi bought {gift_quantity} {gift_type} of {team_name} for {total_money:.2f} lv.")
            elif gift_type == "posters":
                total_money = gift_quantity * 5.35
                print(f"Pepi bought {gift_quantity} {gift_type} of {team_name} for {total_money:.2f} lv.")
            elif gift_type == "stickers":
                total_money = gift_quantity * 1.20
                print(f"Pepi bought {gift_quantity} {gift_type} of {team_name} for {total_money:.2f} lv.")
        elif team_name == "Croatia":
            if gift_type == "flags":
                total_money = gift_quantity * 2.75
                print(f"Pepi bought {gift_quantity} {gift_type} of {team_name} for {total_money:.2f} lv.")
            elif gift_type == "caps":
                total_money = gift_quantity * 6.90
                print(f"Pepi bought {gift_quantity} {gift_type} of {team_name} for {total_money:.2f} lv.")
            elif gift_type == "posters":
                total_money = gift_quantity * 4.95
                print(f"Pepi bought {gift_quantity} {gift_type} of {team_name} for {total_money:.2f} lv.")
            elif gift_type == "stickers":
                total_money = gift_quantity * 1.10
                print(f"Pepi bought {gift_quantity} {gift_type} of {team_name} for {total_money:.2f} lv.")
        elif team_name == "Denmark":
            if gift_type == "flags":
                total_money = gift_quantity * 3.10
                print(f"Pepi bought {gift_quantity} {gift_type} of {team_name} for {total_money:.2f} lv.")
            elif gift_type == "caps":
                total_money = gift_quantity * 6.50
                print(f"Pepi bought {gift_quantity} {gift_type} of {team_name} for {total_money:.2f} lv.")
            elif gift_type == "posters":
                total_money = gift_quantity * 4.80
                print(f"Pepi bought {gift_quantity} {gift_type} of {team_name} for {total_money:.2f} lv.")
            elif gift_type == "stickers":
                total_money = gift_quantity * 0.90
                print(f"Pepi bought {gift_quantity} {gift_type} of {team_name} for {total_money:.2f} lv.")
    else:
        print("Invalid stock!")

else:
    print("Invalid country!")

