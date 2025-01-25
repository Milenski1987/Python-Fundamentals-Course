def tribonacci(sequence, limit):
    next_number = 1
    while len(tribonacci_sequence) < length:
        tribonacci_sequence.append(next_number)

        next_number = sum(tribonacci_sequence[-3:])
    return sequence


length = int(input())
tribonacci_sequence = []
tribonacci_sequence = tribonacci(tribonacci_sequence, length)

print(*tribonacci_sequence, sep=" ")

