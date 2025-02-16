def add(sequence: list[str], current_value: str) -> list[str]:
    sequence.append(current_value)
    return sequence


def remove(sequence: list[str], current_value: str) -> list[str]:
    if current_value in sequence:
        sequence.remove(current_value)
    return sequence


def replace(sequence: list[str], current_value: str, replacement: str) -> list[str]:
    if current_value in sequence:
        sequence[sequence.index(current_value)] = replacement
    return sequence


def collapse(sequence: list[str], current_value: str) -> list[str]:
    filtered_sequence = [number for number in sequence if int(number) >= int(current_value)]
    return filtered_sequence

def main():
    initial_sequence = input().split()

    while True:
        command = input()

        if command == "Finish":
            print(" ".join(initial_sequence))
            break

        action = command.split()[0]

        if action == "Add":
            value = command.split()[1]
            initial_sequence = add(initial_sequence, value)
        elif action == "Remove":
            value = command.split()[1]
            initial_sequence = remove(initial_sequence, value)
        elif action == "Replace":
            value = command.split()[1]
            new_value = command.split()[2]
            initial_sequence = replace(initial_sequence, value, new_value)
        elif action == "Collapse":
            value = command.split()[1]
            initial_sequence = collapse(initial_sequence, value)


main()