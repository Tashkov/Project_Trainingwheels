last_sector = input().upper()  # letter from B - Z in CAPS
rows_in_sector_A = int(input())  # from 1 - 100
seats_per_odd_row = int(input())  # from 1 - 24

seats_per_even_row = seats_per_odd_row + 2
rows = rows_in_sector_A
all_seats = 0

# 65 - 90 = A - Z in ASCII
# 97 - 122 = a - z in ASCII

for sector in range(65, ord(last_sector) + 1):
    if sector == 65:
        for row in range(1, rows + 1):
            if row % 2 != 0:
                for seat in range(97, 97 + seats_per_odd_row):
                    all_seats += 1
                    print(f"{chr(sector)}{row}{chr(seat)}")
            elif row % 2 == 0:
                for seat in range(97, 97 + seats_per_even_row):
                    all_seats += 1
                    print(f"{chr(sector)}{row}{chr(seat)}")
    else:
        # each new sector receives an additional row
        rows += 1
        for row in range(1, rows + 1):
            if row % 2 != 0:
                for seat in range(97, 97 + seats_per_odd_row):
                    all_seats += 1
                    print(f"{chr(sector)}{row}{chr(seat)}")
            elif row % 2 == 0:
                for seat in range(97, 97 + seats_per_even_row):
                    all_seats += 1
                    print(f"{chr(sector)}{row}{chr(seat)}")
print(all_seats)
