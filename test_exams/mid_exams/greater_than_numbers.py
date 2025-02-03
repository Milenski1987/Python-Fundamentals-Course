def average_num(sequence: list) -> int:
    average_of_sequence = sum(sequence) // len(sequence)
    return average_of_sequence


def main():
    integers_sequence = [int(number) for number in input().split()]

    average_number = average_num(integers_sequence)
    result_sequence = [number for number in integers_sequence if number > average_number]
    result_sequence.sort(reverse=True)
    result_sequence = result_sequence[:5]

    if result_sequence:
        print(*result_sequence, sep=" ")
    else:
        print("No")


main()
