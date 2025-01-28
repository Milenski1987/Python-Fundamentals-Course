numbers = [int(number) for number in input().split(", ")]
indices = []

for index, value in enumerate(numbers):
    if value % 2 == 0:
        indices.append(index)

print(indices)