fire_cells = input().split("#")
water_available = int(input())

fire_cell_putted_out = []
effort_level = 0
total_fire = 0

for cell in fire_cells:
    current_cell = cell.split(" = ")
    cell_range = current_cell[0]
    cell_value = int(current_cell[1])

    if (cell_range == "High" and cell_value in range(81, 126)) \
            or (cell_range == "Medium" and cell_value in range(51, 81)) \
            or (cell_range == "Low" and cell_value in range(1, 51)):
        if water_available - cell_value >= 0:
            effort_level += cell_value * 0.25
            total_fire += cell_value
            water_available -= cell_value
            fire_cell_putted_out.append(cell_value)
    else:
        continue

print("Cells:")
for cell in fire_cell_putted_out:
    print(f"- {cell}")
print(f"Effort: {effort_level:.2f}")
print(f"Total Fire: {total_fire}")