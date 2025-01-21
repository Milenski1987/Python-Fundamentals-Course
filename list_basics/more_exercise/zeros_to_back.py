numbers = [int(number) for number in input().split(", ")]
zeros = []

for index in range(len(numbers) - 1, -1, -1):
    if numbers[index] == 0:
        zeros.append(numbers[index])
        numbers.pop(index)

numbers = numbers + zeros
print(numbers)