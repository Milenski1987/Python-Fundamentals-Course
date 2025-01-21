number_count = int(input())

numbers = []

for _ in range(number_count):
    number = int(input())
    numbers.append(number)

command = input()

if command == "even":
    numbers = [number for number in numbers if number % 2 == 0]
elif command == "odd":
    numbers = [number for number in numbers if number % 2 != 0]
elif command == "negative":
    numbers = [number for number in numbers if number < 0]
elif command == "positive":
    numbers = [number for number in numbers if number >= 0]

print(numbers)