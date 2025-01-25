def sum_numbers(num1, num2):
    return num1 + num2


def subtract(num3):
    sum_result = sum_numbers(first_number, second_number)
    return sum_result - num3


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(subtract(third_number))

