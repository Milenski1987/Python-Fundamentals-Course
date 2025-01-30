def calculation(action, num1, num2):
    if action == "multiply":
        return num1 * num2
    elif action == "divide":
        return num1 // num2
    elif action == "add":
        return num1 + num2
    elif action == "subtract":
        return num1 - num2


operator = input()
first_number = int(input())
second_number = int(input())
result = calculation(operator, first_number,second_number)
print(result)