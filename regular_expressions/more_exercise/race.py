import re

names_pattern = r"[A-Za-z]"
distance_pattern = r"\d"

drivers = input().split(", ")
drivers_data = {}
for driver in drivers:
    if driver not in drivers_data:
        drivers_data[driver] = 0


while True:
    command = input()

    if command == "end of race":
        break

    names = re.findall(names_pattern, command)
    distance = re.findall(distance_pattern, command)

    current_driver = ""
    current_distance = 0

    for letter in names:
        current_driver += letter
    for digit in distance:
        current_distance += int(digit)

    if current_driver in drivers_data:
        drivers_data[current_driver] += current_distance


drivers_data = sorted(drivers_data.items(), key= lambda item: -item[1])


print(f"1st place: {drivers_data[0][0]}")
print(f"2nd place: {drivers_data[1][0]}")
print(f"3rd place: {drivers_data[2][0]}")
