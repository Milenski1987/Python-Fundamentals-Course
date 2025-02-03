def find_characters(some_string: str, characters_storage: dict) -> dict:
    for character in some_string:
        if character != " ":
            if character not in characters_storage:
                characters_storage[character] = 0
            characters_storage[character] += 1

    return characters_storage


def main():
    current_string = input()
    characters_dictionary = {}
    characters_dictionary = find_characters(current_string, characters_dictionary)

    for character, occurrence in characters_dictionary.items():
        print(f"{character} -> {occurrence}")


main()
