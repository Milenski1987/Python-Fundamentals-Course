def merge(data: list, first_index: int, second_index: int) -> list:
    if first_index < 0:
        first_index = 0
    if second_index > len(data) - 1:
        second_index = len(data) - 1
    merged_data = data[first_index: second_index + 1]
    data = data[:first_index] + data[second_index + 1:]
    data.insert(first_index, "".join(merged_data))
    return data


def divide(data: list, current_index: int, parts: int) -> list:
    divided_item = []
    item_for_divide = data.pop(current_index)
    elements_to_divide = len(item_for_divide) // parts

    if parts > 0:
        for _ in range(parts - 1):
            divided_item.append(item_for_divide[:elements_to_divide])
            item_for_divide = item_for_divide[elements_to_divide:]

        if len(item_for_divide) > 0:
            divided_item.append(item_for_divide)
    else:
        divided_item.append(item_for_divide)


    data = data[:current_index] + divided_item + data[current_index:]
    return data


def main():
    data_array = input().split()

    while True:
        command = input()

        if command == "3:1":
            break

        current_command = command.split()
        action = current_command[0]

        if action == "merge":
            start_index = int(current_command[1])
            end_index = int(current_command[2])
            data_array = merge(data_array,start_index,end_index)

        elif action == "divide":
            index = int(current_command[1])
            partitions = int(current_command[2])
            data_array = divide(data_array, index, partitions)

    print(" ".join(data_array))


main()