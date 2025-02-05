def shoot(targets: list, index: int, power: int) -> list:
    if index in range(len(targets)):
        targets[index] -= power
        if targets[index] <= 0:
            targets.pop(index)
    return targets


def add(targets: list, index: int, element: int) -> list:
    if index in range(len(targets)):
        targets.insert(index, element)
    else:
        print("Invalid placement!")
    return targets


def strike(targets: list, index: int, radius: int) -> list:
    start_index = index - radius
    end_index = index + radius
    if start_index in range(len(targets)) and end_index in range(len(targets)):
        targets = targets[:start_index] + targets[end_index + 1:]
    else:
        print("Strike missed!")
    return targets


def main():
    targets_list = [int(number) for number in input().split()]

    while True:
        command = input()
        if command == "End":
            print(*targets_list, sep="|")
            break

        current_command = command.split()
        action = current_command[0]
        current_index = int(current_command[1])
        current_value = int(current_command[2])

        if action == "Shoot":
            targets_list = shoot(targets_list, current_index, current_value)

        elif action == "Add":
            targets_list = add(targets_list, current_index, current_value)

        elif action == "Strike":
            targets_list = strike(targets_list, current_index, current_value)


main()