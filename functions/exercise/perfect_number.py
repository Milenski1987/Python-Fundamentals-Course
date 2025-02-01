def perfect_number(current_number: int) -> str:
    divisors_sum = 0
    for digit in range(1, current_number):
        if current_number % digit == 0:
            divisors_sum += digit

    if divisors_sum == current_number:
        return "We have a perfect number!"
    return "It's not so perfect."


number = int(input())
result = perfect_number(number)

print(result)

