def calculation(action: str, number1: int, number2: int) -> int:
    if action == "multiply":
        return number1 * number2
    elif action == "divide":
        return number1 // number2
    elif action == "add":
        return number1 + number2
    elif action == "subtract":
        return number1 - number2


operator = input()
first_number = int(input())
second_number = int(input())
result = calculation(operator, first_number,second_number)

print(result)