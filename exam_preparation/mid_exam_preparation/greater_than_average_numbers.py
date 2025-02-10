def find_average(numbers: list) -> int:
    return sum(numbers) // len(numbers)


def sort_list(numbers: list, average: int) -> list:
    result = [number for number in numbers if number > average]
    result.sort(reverse=True)
    return result[:5]


def main():
    numbers_sequence = [int(number) for number in input().split()]
    average_value = find_average(numbers_sequence)
    numbers_sequence = sort_list(numbers_sequence, average_value)
    if numbers_sequence:
        print(*numbers_sequence, sep=" ")
    else:
        print("No")


main()