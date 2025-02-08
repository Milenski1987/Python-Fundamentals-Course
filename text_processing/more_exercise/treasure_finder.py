import re


def find_type_and_coordinates(keys_sequence: list, current_command: str) -> str:
    treasure_string = ""

    key_index = 0
    for command_index in range(len(current_command)):
        if key_index > len(keys_sequence) - 1:
            key_index = 0

        treasure_string += chr(ord(current_command[command_index]) - keys_sequence[key_index])
        key_index += 1

    type_pattern = r"&([A-Za-z]+)&"
    coordinates_pattern = r"<([A-Za-z0-9]+)>"

    treasure_type = re.findall(type_pattern, treasure_string)[0]
    treasure_coordinates = re.findall(coordinates_pattern, treasure_string)[0]

    return f"Found {treasure_type} at {treasure_coordinates}"


def main():
    keys = [int(number) for number in input().split()]

    while True:
        command = input()

        if command == "find":
            break

        result = find_type_and_coordinates(keys, command)
        print(result)


main()