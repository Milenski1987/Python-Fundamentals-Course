def sum_numbers(number1: int, number2: int) -> int:
    return number1 + number2


def subtract(current_result: int, number3: int) -> int:
    return current_result - number3


def add_and_subtract(number1: int, number2: int, number3: int) -> int:
    sum_result = sum_numbers(number1, number2)
    result = subtract(sum_result, number3)
    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())
final_result = add_and_subtract(first_number, second_number, third_number)

print(final_result)

