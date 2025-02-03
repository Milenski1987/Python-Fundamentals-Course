def create_resources_data(current_input: str, current_list: list) -> list:
    current_list.append(current_input)
    return current_list


def create_dictionary_with_resources(current_list: list, current_dictionary: dict) -> dict:
    for index in range(0, len(current_list), 2):
        if current_list[index] not in current_dictionary:
            current_dictionary[current_list[index]] = 0
        current_dictionary[current_list[index]] += int(current_list[index + 1])
    return current_dictionary


def main():
    resources_dictionary = {}
    resources_list = []
    command = input()
    counter = 0

    while command != "stop":
        resources_list = create_resources_data(command, resources_list)
        command = input()

    resources_dictionary = create_dictionary_with_resources(resources_list, resources_dictionary)

    for resource, quantity in resources_dictionary.items():
        print(f"{resource} -> {quantity}")


main()