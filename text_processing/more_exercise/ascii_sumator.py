start_character = input()
end_character = input()
some_string = input()

total_sum = 0

for character in some_string:
    if ord(character) in range(ord(start_character) + 1, ord(end_character)):
        total_sum += ord(character)

print(total_sum)