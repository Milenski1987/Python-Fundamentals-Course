def digits_letters_others(current_string: str) -> tuple:
    digits = ""
    letters = ""
    others = ""
    for character in current_string:
        if character.isdigit():
            digits += character
        elif character.isalpha():
            letters += character
        else:
            others += character
    return digits, letters, others


def main():
    some_string = input()
    result = digits_letters_others(some_string)
    print(result[0])
    print(result[1])
    print(result[2])


main()