def smallest(number1: int, number2: int, number3: int) -> int:
    return min(number1, number2, number3)


first_number = int(input())
second_number = int(input())
third_number = int(input())
smallest_number = smallest(first_number, second_number, third_number)

print(smallest_number)
