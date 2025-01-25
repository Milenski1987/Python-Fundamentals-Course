def factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result


def division():
    first_factorial = factorial(first_number)
    second_factorial = factorial(second_number)
    return first_factorial / second_factorial


first_number = int(input())
second_number = int(input())

print(f"{division():.2f}")

