def characters(character1: str, character2: str) -> list:
    characters_result = []
    for digit in range(ord(character1) + 1, ord(character2)):
        characters_result.append(chr(digit))
    return characters_result


first_char = input()
second_char = input()
result = characters(first_char, second_char)

print(" ".join(result))
