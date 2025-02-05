def find_average(numbers: list) -> int:
    return sum(numbers) // len(numbers)


def sort_list(numbers: list, average: int) -> list:
    counter = 0
    result = []
    for number in numbers:
        if number > average:
            result.append(number)
            counter += 1
            if counter == 5:
                break
    return result


def main():
    numbers_sequence = [int(number) for number in input().split()]
    average_value = find_average(numbers_sequence)
    numbers_sequence.sort(reverse=True)
    numbers_sequence = sort_list(numbers_sequence, average_value)
    if numbers_sequence:
        print(*numbers_sequence, sep=" ")
    else:
        print("No")


main()