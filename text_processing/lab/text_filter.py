def replace_banned_words(bad_words: list, current_text: str) -> str:
    for word in bad_words:
        if word in current_text:
            good_string = len(word) * "*"
            current_text = current_text.replace(word, good_string)
    return current_text


def main():
    banned_words = input().split(", ")
    text = input()
    result_text = replace_banned_words(banned_words, text)

    print(result_text)


main()