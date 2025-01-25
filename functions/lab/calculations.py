def calculation(action, num1, num2):
    result = 0

    if action == "multiply":
        result = num1 * num2
    elif action == "divide":
        result = num1 // num2
    elif action == "add":
        result = num1 + num2
    elif action == "subtract":
        result = num1 - num2

    return result


operator = input()
first_number = int(input())
second_number = int(input())

print(calculation(operator, first_number, second_number))