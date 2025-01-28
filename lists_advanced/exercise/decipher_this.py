secret_message = input().split()
message = []

for element in secret_message:
    word_list = []
    first_character = ""
    for character in element:
        if character.isdigit():
            first_character += character
        else:
            word_list.append(character)

    first_character = chr(int(first_character))
    word_list.insert(0,first_character)
    word_list[1] , word_list[-1] = word_list[-1], word_list[1]

    word = "".join(word_list)
    message.append(word)



print(" ".join(message))
