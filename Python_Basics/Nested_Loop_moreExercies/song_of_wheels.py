n = int(input())  # 4 - 144

counter = 0
control_number = ""
check = 0
for a in range(1, 10):
    for b in range(1, 10):
        if b > a:
            for c in range(1, 10):
                for d in range(1, 10):
                    if d < c:
                        if (a*b) + (c*d) == n:
                            print(f"{a}{b}{c}{d}", end=" ")
                            counter += 1
                            if counter == 4:
                                control_number = f"{a}{b}{c}{d}"
                        elif (a*b) + (c*d) != n:
                            check = 1
if counter >= 4:
    print(f"\nPassword: {control_number}")
elif check == 1:
    print(f"\nNo!")
