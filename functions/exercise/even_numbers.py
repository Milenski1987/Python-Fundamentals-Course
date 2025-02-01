def even(number: int) -> bool:
    return number % 2 == 0


numbers = [int(current_number) for current_number in input().split()]
result = list(filter(even, numbers))

print(result)
