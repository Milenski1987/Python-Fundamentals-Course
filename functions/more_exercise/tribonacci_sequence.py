def tribonacci(limit: int) -> list:
    sequence = []
    next_number = 1
    while len(sequence) < length:
        sequence.append(next_number)

        next_number = sum(sequence[-3:])
    return sequence


length = int(input())
result = tribonacci(length)

print(*result, sep=" ")

