def find_characters(current_element: str) -> str:
    word_list = []
    first_character = ""
    for character in current_element:
        if character.isdigit():
            first_character += character
        else:
            word_list.append(character)

    first_character = chr(int(first_character))
    word_list.insert(0, first_character)
    word_list[1], word_list[-1] = word_list[-1], word_list[1]

    return "".join(word_list)


secret_message = input().split()
message = []

for element in secret_message:
    result = find_characters(element)
    message.append(result)

print(" ".join(message))
