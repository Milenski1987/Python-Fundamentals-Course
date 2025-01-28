numbers = input().split()
some_string = input()
message = ""

for number in numbers:
    index = 0

    for digit in number:
        index += int(digit)

    index %= len(some_string)

    message += some_string[index]
    some_string = some_string.replace(some_string[index], "", 1)

print(message)