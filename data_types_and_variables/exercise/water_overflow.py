number_of_lines = int(input())
tank_capacity = 255
liters_in_tank = 0
for _ in range(number_of_lines):
    water_to_pour = int(input())

    if tank_capacity - water_to_pour < 0:
        print("Insufficient capacity!")
        continue
    else:
        tank_capacity -= water_to_pour
        liters_in_tank += water_to_pour

print(liters_in_tank)