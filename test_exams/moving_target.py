def shoot(target_list, idx, pwr):
    if idx in range(len(target_list)):
        target_list[idx] -= pwr
        if target_list[idx] <= 0:
            target_list.pop(idx)
    return target_list


def add(target_list, idx, val):
    if idx in range(len(target_list)):
        target_list.insert(idx, val)
    else:
        print("Invalid placement!")
    return target_list


def strike(target_list, idx, rad):
    start_radius_index = idx - rad
    end_radius_index = idx + rad
    if start_radius_index in range(len(target_list)) and end_radius_index in range(len(target_list)):
        target_list = target_list[:start_radius_index] + target_list[end_radius_index + 1:]
    else:
        print("Strike missed!")
    return target_list





targets = [int(number) for number in input().split()]

while True:
    command = input()

    if command == "End":
        print(*targets,sep="|")
        break

    current_command = command.split()
    action = current_command[0]
    index = int(current_command[1])

    if action == "Shoot":
        power = int(current_command[2])
        targets = shoot(targets, index, power)

    elif action == "Add":
        value = int(current_command[2])
        targets = add(targets, index, value)

    elif action == "Strike":
        radius = int(current_command[2])
        targets = strike(targets, index, radius)
