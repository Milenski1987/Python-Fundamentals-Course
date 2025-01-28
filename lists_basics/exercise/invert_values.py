numbers = [int(number) for number in input().split()]

for index in range(len(numbers)):
    numbers[index] = -numbers[index]

print(numbers)