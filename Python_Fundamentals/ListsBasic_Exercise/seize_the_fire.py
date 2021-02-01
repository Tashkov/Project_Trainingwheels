fire_cells = input().split("#")  # <- each fire is split with
water = int(input())
effort = 0
total_fire = 0
lst_put_out_cells = []

for cell in fire_cells:
    current_cell = cell.split()
    if current_cell[0] == "High" and 81 <= int(current_cell[2]) <= 125:
        if water >= int(current_cell[2]):
            water -= int(current_cell[2])
            total_fire += int(current_cell[2])
            effort += int(current_cell[2]) * 0.25
            lst_put_out_cells.append(int(current_cell[2]))
    elif current_cell[0] == "Medium" and 51 <= int(current_cell[2]) <= 80:
        if water >= int(current_cell[2]):
            water -= int(current_cell[2])
            total_fire += int(current_cell[2])
            effort += int(current_cell[2]) * 0.25
            lst_put_out_cells.append(int(current_cell[2]))
    elif current_cell[0] == "Low" and 1 <= int(current_cell[2]) <= 50:
        if water >= int(current_cell[2]):
            water -= int(current_cell[2])
            total_fire += int(current_cell[2])
            effort += int(current_cell[2]) * 0.25
            lst_put_out_cells.append(int(current_cell[2]))
print("Cells:")
for put_out_cell in lst_put_out_cells:

    print(f'- {put_out_cell}')

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')

