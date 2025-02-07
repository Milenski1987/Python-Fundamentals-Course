def find_emoji(some_string: str) -> list:
    current_emoji = []
    for index in range(len(some_string)):
        if some_string[index] == ":":
            if index != len(some_string) -1 :
                this_emoji = ""
                this_emoji += some_string[index]
                this_emoji += some_string[index + 1]
                current_emoji.append(this_emoji)
    return current_emoji


def main():
    text = input()
    emojis = find_emoji(text)

    for emoji in emojis:
        print(emoji)


main()