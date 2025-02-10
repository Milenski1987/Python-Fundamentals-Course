def swap(array: list[int], index1: int, index2: int) -> list[int]:
    array[index1], array[index2] = array[index2], array[index1]
    return array


def multiply(array: list[int], index1: int, index2: int) -> list[int]:
    array[index1] *= array[index2]
    return array


def decrease(array: list[int]) -> list[int]:
    for index in range(len(array)):
        array[index] -= 1
    return array


def array_modify(array: list[int]) -> str:
    while True:
        command = input()

        if command == "end":
            return ", ".join(map(str, array))


        current_command = command.split()
        action = current_command[0]

        if action == "swap":
            first_index = int(current_command[1])
            second_index = int(current_command[2])
            array = swap(array, first_index, second_index)

        elif action == "multiply":
            first_index = int(current_command[1])
            second_index = int(current_command[2])
            array = multiply(array, first_index, second_index)

        elif action == "decrease":
            array = decrease(array)


def main():
    integers_array = [int(number) for number in input().split()]
    result = array_modify(integers_array)

    print(result)


main()