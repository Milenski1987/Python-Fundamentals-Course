def fire(current_command: str, warship: list[int]) -> list[int]:
    index = int(current_command.split()[1])
    damage = int(current_command.split()[2])

    if index in range(len(warship)):
        warship[index] -= damage
        if warship[index] <= 0:
            warship.clear()
    return warship


def defend(current_command: str, pirate_ship: list[int]) -> list[int]:
    start_index = int(current_command.split()[1])
    end_index = int(current_command.split()[2])
    damage = int(current_command.split()[3])

    if start_index in range(len(pirate_ship)) and end_index in range(len(pirate_ship)):
        for index in range(start_index, end_index + 1):
            pirate_ship[index] -= damage
            if pirate_ship[index] <= 0:
                pirate_ship.clear()
                break
    return pirate_ship


def repair(current_command: str, pirate_ship: list[int], max_health: int) -> list[int]:
    index = int(current_command.split()[1])
    health = int(current_command.split()[2])

    if index in range(len(pirate_ship)):
        pirate_ship[index] += health
        if pirate_ship[index] > max_health:
            pirate_ship[index] = max_health
    return pirate_ship


def status(pirate_ship: list[int], max_health: int) -> int:
    counter = 0
    for section in pirate_ship:
        if section < max_health * 0.20:
            counter += 1
    return counter


def war(pirate_ship: list[int], warship: list[int], max_health: int) -> str:

    while True:
        command = input()
        if command == "Retire":
            return f"Pirate ship status: {sum(pirate_ship)}\nWarship status: {sum(warship)}"
        action = command.split()[0]
        if action == "Fire":
            warship = fire(command, warship)
        elif action == "Defend":
            pirate_ship = defend(command, pirate_ship)
        elif action == "Repair":
            pirate_ship = (repair(command, pirate_ship, max_health))
        elif action == "Status":
            current_status = status(pirate_ship, max_health)
            print(f"{current_status} sections need repair.")

        if not warship:
            return "You won! The enemy ship has sunken."
        if not pirate_ship:
            return "You lost! The pirate ship has sunken."


def main():
    pirate_ship_status = list(map(int, input().split(">")))
    warship_status = list(map(int, input().split(">")))
    max_section_health = int(input())

    result = war(pirate_ship_status, warship_status, max_section_health)
    print(result)


main()