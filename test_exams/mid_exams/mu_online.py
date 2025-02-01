def potion_command(health: int, potion_amount: int) -> tuple:
    current_health = health
    health += potion_amount
    if health > 100:
        health = 100
    health_diff = health - current_health
    potion_command_result = f"You healed for {health_diff} hp.\nCurrent health: {health} hp."
    return health, potion_command_result


def chest_command(bitcoins:int, amount: int) -> tuple:
    bitcoins += amount
    chest_command_result = f"You found {amount} bitcoins."
    return bitcoins, chest_command_result


def monster_found(name: str, power: int, health: int) -> tuple:
    health -= power
    monster_command_result = ""
    if health > 0:
        monster_command_result = f"You slayed {name}."
    else:
        monster_command_result = f"You died! Killed by {name}."
    return health, monster_command_result


def main():
    dungeon_rooms = input().split("|")
    initial_health = 100
    initial_bitcoins = 0
    room_count = 0

    for room in dungeon_rooms:
        room_count += 1

        command, value = room.split()
        value = int(value)

        if command == "potion":
            initial_health, result = potion_command(initial_health, value)
            print(result)

        elif command == "chest":
            initial_bitcoins, result = chest_command(initial_bitcoins, value)
            print(result)

        else:
            initial_health, result = monster_found(command, value, initial_health)
            print(result)

        if initial_health <= 0:
            print(f"Best room: {room_count}")
            break

    else:
        print(f"You've made it!\nBitcoins: {initial_bitcoins}\nHealth: {initial_health}")


main()