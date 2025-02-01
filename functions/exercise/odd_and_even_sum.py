def sum_odd_even(current_number: str) -> str:
    even_sum = 0
    odd_sum = 0
    for digit in current_number:
        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number_as_string = input()
result = sum_odd_even(number_as_string)

print(result)
