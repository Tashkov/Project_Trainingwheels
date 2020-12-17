age = float(input())
sex = input()

if sex == "f":
    if age >=16:
        print("Ms.")
    elif age <16:
        print("Miss")
elif sex == "m":
    if age >=16:
        print("Mr.")
    elif age < 16:
        print("Master")