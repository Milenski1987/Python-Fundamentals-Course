def loot(chest: list, looted_items: list) -> list:
    for item in looted_items:
        if item not in chest:
            chest.insert(0, item)
    return chest


def drop(chest: list, index: int) -> list:
    if index in range(len(chest)):
        item_to_drop = chest.pop(index)
        chest.append(item_to_drop)
    return chest


def steal(chest: list, count: int) -> list:
    stolen_items = chest[-count:]
    chest = chest[:-count]
    if stolen_items:
        print(", ".join(stolen_items))
    return chest


def calculate_average_gain(chest: list) -> float:
    length = 0
    for element in chest:
        length += len(element)
    average = length / len(chest)
    return average


def main():
    treasure_chest = input().split("|")
    while True:
        command = input()
        if command == "Yohoho!":
            break
        current_command = command.split()
        action = current_command[0]

        if action == "Loot":
            current_loot = current_command[1:]
            treasure_chest = loot(treasure_chest, current_loot)

        elif action == "Drop":
            current_index = int(current_command[1])
            treasure_chest = drop(treasure_chest, current_index)

        elif action == "Steal":
            current_count = int(current_command[1])
            treasure_chest = steal(treasure_chest, current_count)

    if treasure_chest:
        average_gain = calculate_average_gain(treasure_chest)
        print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
    else:
        print("Failed treasure hunt.")


main()