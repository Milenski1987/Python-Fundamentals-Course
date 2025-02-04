def create_force_data(sides_data: dict, side: str, user: str) -> dict:
    already_user = False
    for current_side, current_users in sides_data.items():
        if user in current_users:
            already_user = True
            break
    if not already_user and side not in sides_data:
        sides_data[side] = []
        sides_data[side].append(user)

    elif not already_user:
        sides_data[side].append(user)

    return sides_data


def check_for_existing_users(side_data: dict, side: str, user: str) -> dict:
    already_user = False
    current_user_side = ""
    for current_side, current_users in side_data.items():
        if user in current_users:
            current_user_side = current_side
            already_user = True
            break

    if side not in side_data:
        side_data[side] = []

    if not already_user:
        side_data[side].append(user)

    else:
        side_data[current_user_side].remove(user)
        side_data[side].append(user)

    print(f"{user} joins the {side} side!")
    return side_data


def main():
    force_sides = {}

    while True:
        command = input()

        if command == "Lumpawaroo":
            break

        if "|" in command:
            force_side, force_user = command.split(" | ")
            force_sides = create_force_data(force_sides, force_side, force_user)

        elif "->" in command:
            force_user, force_side = command.split(" -> ")
            force_sides = check_for_existing_users(force_sides, force_side, force_user)

    for side, users in force_sides.items():
        if users:
            print(f"Side: {side}, Members: {len(users)}")
            for user in users:
                print(f"! {user}")


main()