def loot(chest: list, current_loot: list) -> list:
    for item in current_loot:
        if item not in chest:
            chest.insert(0, item)
    return chest


def drop(chest: list, current_index: int) -> list:
    if current_index in range(len(chest)):
        removed_item = chest.pop(current_index)
        chest.append(removed_item)
    return chest


def steal(chest: list, counter: int) -> list:
    stolen_items = chest[-counter:]
    chest = chest[:-counter]
    print(", ".join(stolen_items))
    return chest


def calculate_average_gain(chest: list) -> float:
    result = 0
    for item in chest:
        result += len(item)
    average = result / len(chest)
    return average


def main():
    initial_chest = input().split("|")

    while True:
        command = input()

        if command == "Yohoho!":
            break

        current_command = command.split()
        action = current_command[0]

        if action == "Loot":
            picked_loot = current_command[1:]
            initial_chest = loot(initial_chest, picked_loot)

        elif action == "Drop":
            index = int(current_command[1])
            initial_chest = drop(initial_chest, index)

        elif action == "Steal":
            count = int(current_command[1])
            initial_chest = steal(initial_chest, count)

    if initial_chest:
        print(f"Average treasure gain: {calculate_average_gain(initial_chest):.2f} pirate credits.")
    else:
        print("Failed treasure hunt.")


main()