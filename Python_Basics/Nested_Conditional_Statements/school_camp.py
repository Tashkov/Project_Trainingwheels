season = input()  # Winter, Spring or Summer
group_type = input()  # boys, girls or mixed
students_number = int(input())  # num [1...1000]
stays_total = int(input())  # num [1...100]

sport_type = ""
total_money = 0

if students_number >= 50:  # apply 50% discount to final price
    if season == "Winter":
        if group_type == "boys" or group_type == "girls":
            total_money = (students_number * 9.60) * stays_total
            if group_type == "boys":
                sport_type = "Judo"
            elif group_type == "girls":
                sport_type = "Gymnastics"
        else:
            total_money = (students_number * 10) * stays_total
            sport_type = "Ski"
    elif season == "Spring":
        if group_type == "boys" or group_type == "girls":
            total_money = (students_number * 7.20) * stays_total
            if group_type == "boys":
                sport_type = "Tennis"
            elif group_type == "girls":
                sport_type = "Athletics"
        else:
            sport_type = "Cycling"
            total_money = (students_number * 9.50) * stays_total
    elif season == "Summer":
        if group_type == "boys" or group_type == "girls":
            total_money = (students_number * 15) * stays_total
            if group_type == "boys":
                sport_type = "Football"
            elif group_type == "girls":
                sport_type = "Volleyball"
        else:
            sport_type = "Swimming"
            total_money = (students_number * 20) * stays_total

    total_money *= 0.50

elif 20 <= students_number < 50:  # apply 15% discount to final price
    if season == "Winter":
        if group_type == "boys" or group_type == "girls":
            total_money = (students_number * 9.60) * stays_total
            if group_type == "boys":
                sport_type = "Judo"
            elif group_type == "girls":
                sport_type = "Gymnastics"
        else:
            sport_type = "Ski"
            total_money = (students_number * 10) * stays_total
    elif season == "Spring":
        if group_type == "boys" or group_type == "girls":
            total_money = (students_number * 7.20) * stays_total
            if group_type == "boys":
                sport_type = "Tennis"
            elif group_type == "girls":
                sport_type = "Athletics"
        else:
            sport_type = "Cycling"
            total_money = (students_number * 9.50) * stays_total
    elif season == "Summer":
        if group_type == "boys" or group_type == "girls":
            total_money = (students_number * 15) * stays_total
            if group_type == "boys":
                sport_type = "Football"
            elif group_type == "girls":
                sport_type = "Volleyball"
        else:
            sport_type = "Swimming"
            total_money = (students_number * 20) * stays_total

    total_money *= 0.85
elif 10 <= students_number < 20:  # apply 5% discount to final price
    if season == "Winter":
        if group_type == "boys" or group_type == "girls":
            total_money = (students_number * 9.60) * stays_total
            if group_type == "boys":
                sport_type = "Judo"
            elif group_type == "girls":
                sport_type = "Gymnastics"
        else:
            sport_type = "Ski"
            total_money = (students_number * 10) * stays_total
    elif season == "Spring":
        if group_type == "boys" or group_type == "girls":
            total_money = (students_number * 7.20) * stays_total
            if group_type == "boys":
                sport_type = "Tennis"
            elif group_type == "girls":
                sport_type = "Athletics"
        else:
            sport_type = "Cycling"
            total_money = (students_number * 9.50) * stays_total
    elif season == "Summer":
        if group_type == "boys" or group_type == "girls":
            total_money = (students_number * 15) * stays_total
            if group_type == "boys":
                sport_type = "Football"
            elif group_type == "girls":
                sport_type = "Volleyball"
        else:
            sport_type = "Swimming"
            total_money = (students_number * 20) * stays_total

    total_money *= 0.95

elif students_number < 10:
    if season == "Winter":
        if group_type == "boys" or group_type == "girls":
            total_money = (students_number * 9.60) * stays_total
            if group_type == "boys":
                sport_type = "Judo"
            elif group_type == "girls":
                sport_type = "Gymnastics"
        else:
            sport_type = "Ski"
            total_money = (students_number * 10) * stays_total
    elif season == "Spring":
        if group_type == "boys" or group_type == "girls":
            total_money = (students_number * 7.20) * stays_total
            if group_type == "boys":
                sport_type = "Tennis"
            elif group_type == "girls":
                sport_type = "Athletics"
        else:
            sport_type = "Cycling"
            total_money = (students_number * 9.50) * stays_total
    elif season == "Summer":
        if group_type == "boys" or group_type == "girls":
            total_money = (students_number * 15) * stays_total
            if group_type == "boys":
                sport_type = "Football"
            elif group_type == "girls":
                sport_type = "Volleyball"
        else:
            sport_type = "Swimming"
            total_money = (students_number * 20) * stays_total

print(f"{sport_type} {total_money:.2f} lv.")