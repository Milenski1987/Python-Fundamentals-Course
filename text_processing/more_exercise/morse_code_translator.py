def translate_message(words: list, translator: dict) -> str:
    translated_message_as_list = []

    for word in words:
        translated_word = ""
        letters = word.split()
        for letter in letters:
            translated_word += translator[letter]
        translated_message_as_list.append(translated_word)

    return " ".join(translated_message_as_list)


def main():
    morse_message_words = input().split(" | ")

    morse_code = {
        ".-": "A",
        "-...": "B",
        "-.-.": "C",
        "-..": "D",
        ".": "E",
        "..-.": "F",
        "--.": "G",
        "....": "H",
        "..": "I",
        ".---": "J",
        "-.-": "K",
        ".-..": "L",
        "--": "M",
        "-.": "N",
        "---": "O",
        ".--.": "P",
        "--.-": "Q",
        ".-.": "R",
        "...": "S",
        "-": "T",
        "..-": "U",
        "...-": "V",
        ".--": "W",
        "-..-": "X",
        "-.--": "Y",
        "--..": "Z"}

    result = translate_message(morse_message_words, morse_code)
    print(result)


main()