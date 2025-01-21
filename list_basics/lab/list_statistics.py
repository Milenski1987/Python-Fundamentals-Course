number_count = int(input())

positive_numbers = []
negative_numbers = []

for _ in range(number_count):
    number = int(input())

    if number >= 0:
        positive_numbers.append(number)
    else:
        negative_numbers.append(number)

print(positive_numbers)
print(negative_numbers)
print(f"Count of positives: {len(positive_numbers)}\nSum of negatives: {sum(negative_numbers)}")