def create_dwarf_dictionary(data: dict,hat_colors_data: dict, hat_color: str, id_: str, physics: int) -> tuple:
    if id_ not in data:
        data[id_] = physics
        hat_colors_data = colors_counter(hat_colors_data, hat_color)
    if physics > data[id_]:
        data[id_] = physics
    return data, hat_colors_data


def colors_counter(hat_colors_data: dict, hat_color: str) -> dict:
    if hat_color not in hat_colors_data:
        hat_colors_data[hat_color] = 0
    hat_colors_data[hat_color] += 1
    return hat_colors_data


def main():
    dwarfs_data = {}
    hat_colors_counters = {}

    while True:
        command = input()

        if command == "Once upon a time":
            break


        dwarf_name, dwarf_hat_color, dwarf_physics = command.split(" <:> ")
        dwarf_physics = int(dwarf_physics)
        dwarf_id = f"{dwarf_name}:{dwarf_hat_color}"

        dwarfs_data, hat_colors_counters = \
            create_dwarf_dictionary(dwarfs_data,hat_colors_counters,dwarf_hat_color, dwarf_id, dwarf_physics)


    dwarfs_data = dict(
        sorted(dwarfs_data.items(), key=lambda phys: (-phys[1], -hat_colors_counters[phys[0].split(":")[1]])))

    for dwarf_current_id, current_physics in dwarfs_data.items():
        name, color = dwarf_current_id.split(":")
        print(f"({color}) {name} <-> {current_physics}")


main()