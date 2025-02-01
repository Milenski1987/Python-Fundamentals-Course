def collect(items_collection: list, current_item: str) -> list:
    if current_item not in items_collection:
        items_collection.append(current_item)
    return items_collection


def drop(items_collection: list, current_item: str) -> list:
    if current_item in items_collection:
        items_collection.remove(current_item)
    return items_collection


def combine_items(items_collection: list, current_item: str, new_item: str) -> list:
    if current_item in items_collection:
        index_for_new_item = items_collection.index(current_item) + 1
        items_collection.insert(index_for_new_item, new_item)
    return items_collection


def renew(items_collection: list, current_item: str) -> list:
    if current_item in items_collection:
        current_item_index = items_collection.index(current_item)
        removed_item = items_collection.pop(current_item_index)
        items_collection.append(removed_item)
    return items_collection


def main():
    current_items = input().split(", ")

    while True:
        command = input()

        if command == "Craft!":
            print(", ".join(current_items))
            break

        current_command = command.split(" - ")
        action = current_command[0]
        item = current_command[1]

        if action == "Collect":
            current_items = collect(current_items, item)

        elif action == "Drop":
            current_items = drop(current_items, item)

        elif action == "Combine Items":
            first_item, second_item = item.split(":")
            current_items = combine_items(current_items, first_item, second_item)

        elif action == "Renew":
            current_items = renew(current_items, item)


main()