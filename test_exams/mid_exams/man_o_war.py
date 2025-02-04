def fire(war_ship: list, current_index: int, current_damage: int) -> list:
    if current_index in range(len(war_ship)):
        war_ship[current_index] -= current_damage
    return war_ship


def defend(pirate: list, first_index: int, second_index: int, current_damage: int) -> list:
    if first_index in range(len(pirate)) and second_index in range(len(pirate)):
        for current_index in range(first_index, second_index + 1):
            pirate[current_index] -= current_damage
    return pirate


def repair(pirate: list, current_index: int, amount: int, max_health: int) -> list:
    if current_index in range(len(pirate)):
        pirate[current_index] += amount
        if pirate[current_index] > max_health:
            pirate[current_index] = max_health
    return pirate


def status(pirate: list, max_health: int) -> str:
    count = 0
    repair_threshold = max_health * 0.20
    for section in pirate:
        if section < repair_threshold:
            count += 1
    return f"{count} sections need repair."


def check_for_sink(ship_status: list) -> bool:
    for section in ship_status:
        if section <= 0:
            return True
    return False


def main():
    pirate_ship_status = [int(number) for number in input().split(">")]
    warship_status = [int(number) for number in input().split(">")]

    max_health_capacity = int(input())

    while True:
        command = input()

        if command == "Retire":
            print(f"Pirate ship status: {sum(pirate_ship_status)}\nWarship status: {sum(warship_status)}")
            break

        current_command = command.split()
        action = current_command[0]

        if action == "Fire":
            index = int(current_command[1])
            damage = int(current_command[2])
            warship_status = fire(warship_status, index, damage)
            ship_check = check_for_sink(warship_status)
            if ship_check:
                print("You won! The enemy ship has sunken.")
                break

        elif action == "Defend":
            start_index = int(current_command[1])
            end_index = int(current_command[2])
            damage = int(current_command[3])
            pirate_ship_status = defend(pirate_ship_status, start_index, end_index, damage)
            ship_check = check_for_sink(pirate_ship_status)
            if ship_check:
                print("You lost! The pirate ship has sunken.")
                break

        elif action == "Repair":
            index = int(current_command[1])
            health = int(current_command[2])
            pirate_ship_status = repair(pirate_ship_status, index, health, max_health_capacity)


        elif action == "Status":
            result = status(pirate_ship_status, max_health_capacity)
            print(result)


main()