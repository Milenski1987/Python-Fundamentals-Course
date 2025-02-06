def create_dragons_data(dragons_count: int) -> tuple:
    default_health = 250
    default_damage = 45
    default_armor = 10
    data_by_id = {}
    data_by_type = {}

    for _ in range(dragons_count):
        dragon_type, dragon_name, dragon_damage, dragon_health, dragon_armor = input().split()
        dragon_damage =  default_damage if dragon_damage == "null" else int(dragon_damage)
        dragon_health =  default_health if dragon_health == "null" else int(dragon_health)
        dragon_armor = default_armor if dragon_armor == "null" else int(dragon_armor)
        dragon_id = f"{dragon_type}:{dragon_name}"

        if dragon_id not in data_by_id:
            if dragon_type not in data_by_type:
                data_by_type[dragon_type] = []
            data_by_type[dragon_type].append(dragon_name)
        data_by_id[dragon_id] = {"damage": int(dragon_damage), "health": int(dragon_health), "armor": int(dragon_armor)}

    return data_by_id, data_by_type


def calculate_average_stats(data_by_id: dict, dragon_type: str) -> str:
    dragons_count = 0
    total_damage = 0
    total_health = 0
    total_armor = 0

    for id_ in data_by_id:
        if id_.split(":")[0] == dragon_type:
            total_damage += data_by_id[id_]['damage']
            total_health += data_by_id[id_]['health']
            total_armor += data_by_id[id_]['armor']
            dragons_count += 1

    return f"{total_damage / dragons_count:.2f}/{total_health/dragons_count:.2f}/{total_armor/dragons_count:.2f}"

def main():
    number_of_dragons = int(input())

    dragons_data_by_id, dragons_data_by_type = create_dragons_data(number_of_dragons)

    for type_, names in dragons_data_by_type.items():
        sorted_names = sorted(names)
        dragons_data_by_type[type_] = sorted_names

    for type_, names in dragons_data_by_type.items():
        average_stats = calculate_average_stats(dragons_data_by_id, type_)
        print(f"{type_}::({average_stats})")
        for name in names:
            for id_s in dragons_data_by_id:
                id_type, id_name = id_s.split(":")
                if type_ == id_type and name == id_name:
                    damage = dragons_data_by_id[id_s]['damage']
                    health = dragons_data_by_id[id_s]['health']
                    armor = dragons_data_by_id[id_s]['armor']
                    print(f"-{name} -> damage: {damage}, health: {health}, armor: {armor}")


main()