def characters(char1, char2):
    result = []
    for digit in range(ord(char1) + 1, ord(char2)):
        result.append(chr(digit))

    return " ".join(result)


first_char = input()
second_char = input()

print(characters(first_char, second_char))

