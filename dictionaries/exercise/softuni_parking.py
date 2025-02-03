registered_users = {}


def register(name: str, license_number: str) -> str:
    if name in registered_users:
        return f"ERROR: already registered with plate number {license_number}"
    registered_users[name] = license_number
    return f"{name} registered {license_number} successfully"


def unregister(name: str) -> str:
    if name not in registered_users:
        return f"ERROR: user {name} not found"
    del registered_users[name]
    return f"{name} unregistered successfully"


def main():
    number_of_commands = int(input())

    for _ in range(number_of_commands):
        command = input().split()
        action = command[0]
        username = command[1]

        if action == "register":
            license_plate = command[2]
            result = register(username, license_plate)
            print(result)

        elif action == "unregister":
            result = unregister(username)
            print(result)

    for user, plate in registered_users.items():
        print(f"{user} => {plate}")


main()