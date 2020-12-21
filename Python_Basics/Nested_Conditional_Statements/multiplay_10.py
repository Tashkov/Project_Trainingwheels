line = float(input())  # read new line until negative num

while float(line) >= 0:
    line *= 2
    print(f"Result: {line:.2f}")
    line = float(input())
print("Negative number!")
