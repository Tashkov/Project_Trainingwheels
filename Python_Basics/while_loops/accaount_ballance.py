n = input()
balance = 0.0

while n != "NoMoreMoney":
    increase = float(n)
    if increase < 0:
        print("Invalid operation!")
        break
    balance += increase
    print(f"Increase: {increase:.2f}")
    n = input()
print(f'Total: {balance:.2f}')