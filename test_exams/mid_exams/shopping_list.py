def urgent(groceries_data: list[str], current_item: str) -> list[str]:
    if current_item not in groceries_data:
        groceries_data.insert(0, current_item)
    return groceries_data


def unnecessary(groceries_data: list[str], current_item: str) -> list[str]:
    if current_item in groceries_data:
        groceries_data.remove(current_item)
    return groceries_data


def correct(groceries_data: list[str], old_item, new_item) -> list[str]:
    if old_item in groceries_data:
        groceries_data[groceries_data.index(old_item)] = new_item
    return groceries_data


def rearrange(groceries_data: list[str], current_item: str) -> list[str]:
    if current_item in groceries_data:
        groceries_data.remove(current_item)
        groceries_data.append(current_item)
    return groceries_data

def manipulate_groceries(groceries_data: list[str]) -> list[str]:

    while True:
        command = input()

        if command == "Go Shopping!":
            break

        action = command.split()[0]
        if action == "Urgent":
            item = command.split()[1]
            groceries_data = urgent(groceries_data, item)

        elif action == "Unnecessary":
            item = command.split()[1]
            groceries_data = unnecessary(groceries_data, item)

        elif action == "Correct":
            first_item = command.split()[1]
            second_item = command.split()[2]
            groceries_data = correct(groceries_data, first_item, second_item)

        elif action == "Rearrange":
            item = command.split()[1]
            groceries_data = rearrange(groceries_data, item)

    return groceries_data

def main():
    groceries_list = input().split("!")
    groceries_list = manipulate_groceries(groceries_list)

    print(", ".join(groceries_list))


main()