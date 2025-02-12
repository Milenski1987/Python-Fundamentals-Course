def loot(current_command: str, chest: list[str]) -> list[str]:
    current_loot = current_command.split()[1:]
    for item in current_loot:
        if item not in chest:
            chest.insert(0, item)
    return chest


def drop(current_command: str, chest: list[str]) -> list[str]:
    index = int(current_command.split()[1])
    if index in range(len(chest)):
        chest.append(chest.pop(index))
    return chest


def steal(current_command: str, chest: list) -> list[str]:
    count_items = int(current_command.split()[1])
    stolen_items = chest[-count_items:]
    chest = chest[:-count_items]
    print(", ".join(stolen_items))
    return chest


def treasure_hunt(chest: list[str]):

    while True:
        command = input()

        if command == "Yohoho!":
            break

        action = command.split()[0]
        if action == "Loot":
            chest = loot(command, chest)
        elif action == "Drop":
            chest = drop(command, chest)
        elif action == "Steal":
            chest = steal(command, chest)

    return chest


def check_result(chest: list[str]) -> str:
    if chest:
        average_gain = 0
        for item in chest:
            average_gain += len(item)
        average_gain = average_gain / len(chest)

        return f"Average treasure gain: {average_gain:.2f} pirate credits."
    return "Failed treasure hunt."


def main():
    treasure_chest = input().split("|")
    treasure_chest = treasure_hunt(treasure_chest)

    statement = check_result(treasure_chest)
    print(statement)


main()