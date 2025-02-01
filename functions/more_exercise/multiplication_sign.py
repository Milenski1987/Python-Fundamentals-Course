def positive_or_negative(number1: int, number2: int, number3: int) -> str:
    numbers_list = [number1, number2, number3]
    negative_numbers = 0
    for number in numbers_list:
        if number == 0:
            return "zero"
        if number < 0:
            negative_numbers += 1
    if negative_numbers % 2 != 0:
        return "negative"
    return "positive"


first_number = int(input())
second_number = int(input())
third_number = int(input())
result = positive_or_negative(first_number, second_number, third_number)

print(result)

