from math import ceil


def fill_groups_with_numbers(numbers_sequence: list, current_group: int) -> tuple:
    working_list = []
    for index in range(len(numbers_sequence) - 1, -1, -1):
        if numbers_sequence[index] <= current_group:
            found = numbers_sequence.pop(index)
            working_list.append(found)

    working_list.reverse()
    return numbers_sequence, f"Group of {current_group}'s: {working_list}"


def main():
    initial_sequence = [int(number) for number in input().split(", ")]

    number_of_groups = ceil(max(initial_sequence) / 10)

    group_of = 10
    for _ in range(number_of_groups):
        initial_sequence, result = fill_groups_with_numbers(initial_sequence, group_of)
        print(result)
        group_of += 10


main()