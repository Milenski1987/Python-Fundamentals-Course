def positive(sequence: list) -> list:
    result = [number for number in sequence if int(number) >= 0]
    return result


def negative(sequence: list) -> list:
    result = [number for number in sequence if int(number) < 0]
    return result


def even(sequence: list) -> list:
    result = [number for number in sequence if int(number) % 2 == 0]
    return result


def odd(sequence: list) -> list:
    result = [number for number in sequence if int(number) % 2 != 0]
    return result


def main():
    numbers = input().split(", ")
    positive_numbers = positive(numbers)
    negative_numbers = negative(numbers)
    even_numbers = even(numbers)
    odd_numbers = odd(numbers)

    print(f"Positive: {', '.join(positive_numbers)}")
    print(f"Negative: {', '.join(negative_numbers)}")
    print(f"Even: {', '.join(even_numbers)}")
    print(f"Odd: {', '.join(odd_numbers)}")


main()