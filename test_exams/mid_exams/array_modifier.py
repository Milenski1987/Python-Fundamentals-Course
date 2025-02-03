def swap(array: list, index1: int, index2: int) -> list:
    array[index1], array[index2] = array[index2], array[index1]
    return array


def multiply(array: list, index1: int, index2: int) -> list:
    array[index1] *= array[index2]
    return array


def decrease(array: list) -> list:
    for index in range(len(array)):
        array[index] -= 1
    return array


def main():
    integers_array = [int(number) for number in input().split()]

    while True:
        command = input()

        if command == "end":
            print(*integers_array, sep=", ")
            break

        current_command = command.split()
        action = current_command[0]

        if action == "swap":
            first_index = int(current_command[1])
            second_index = int(current_command[2])
            integers_array = swap(integers_array, first_index, second_index)

        elif action == "multiply":
            first_index = int(current_command[1])
            second_index = int(current_command[2])
            integers_array = multiply(integers_array, first_index, second_index)

        elif action == "decrease":
            integers_array = decrease(integers_array)


main()