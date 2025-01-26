sequence = [int(number) for number in input().split()]
result = []

average_value_of_sequence = sum(sequence) // len(sequence)

sequence.sort(reverse=True)
for number in sequence:
    if number > average_value_of_sequence:
        result.append(number)

    if len(result) == 5:
        break

if result:
    result.sort(reverse=True)
    print(*result, sep=" ")
else:
    print("No")
