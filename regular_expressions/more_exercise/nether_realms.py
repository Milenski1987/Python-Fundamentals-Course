import re


def calculate_damage(name: str) -> float:
    current_damage = 0
    damage_pattern = r"([\-]?[\d]+[\.\d]*)"
    damage_result = re.findall(damage_pattern, name)
    if damage_result:
        for damage in damage_result:
            current_damage += float(damage)

    damage_actions = r"([\/\*])"
    actions_results = re.findall(damage_actions, name)
    if actions_results:
        for action in actions_results:
            if action == "*":
                current_damage *= 2
            elif action == "/":
                current_damage /= 2

    return current_damage


def calculate_health(name: str) -> int:
    current_health = 0
    health_pattern = r"([^\d\+\-\*\/\.])"
    health_result = re.findall(health_pattern, name)
    if health_result:
        for character in health_result:
            current_health += ord(character)
    return current_health


def main():
    initial_demons = input().replace(","," ")
    demons = initial_demons.split()

    demons_book = {}
    if demons:
        for demon in demons:
            total_health = calculate_health(demon)
            total_damage = calculate_damage(demon)

            demons_book[demon] = {}
            demons_book[demon] = {"health": total_health, "damage": total_damage}

        demons_book = dict(sorted(demons_book.items()))

    if demons_book:
        for demon in demons_book:
            print(f"{demon} - {demons_book[demon]['health']} health, {demons_book[demon]['damage']:.2f} damage ")


main()