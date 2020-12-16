weather = float(input())

if weather >= 26.00 or weather == 35.00:
    print("Hot")
elif weather >= 20.1 or weather == 25.9:
    print("Warm")
elif weather >= 15.00 or weather == 20.00:
    print("Mild")
elif weather >= 12.00 or weather == 14.9:
    print("Cool")
elif weather >= 5 or weather == 11.9:
    print("Cold")
else:
    print("unknown")