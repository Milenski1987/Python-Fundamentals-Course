def calculate_factorial(number: int) -> int:
    current_result = 1
    for digit in range(1, number + 1):
        current_result *= digit
    return current_result


def division(number1: int, number2: int) -> float:
    first_factorial = calculate_factorial(number1)
    second_factorial = calculate_factorial(number2)
    return first_factorial / second_factorial


first_number = int(input())
second_number = int(input())
result = division(first_number, second_number)

print(f"{result:.2f}")

