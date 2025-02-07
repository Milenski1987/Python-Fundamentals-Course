def processing_the_string(current_string: str) -> float:
    digit = ""
    first_letter = current_string[0]
    last_letter = current_string[-1]
    for character in current_string:
        if character.isdigit():
            digit += character
    digit = int(digit)

    if first_letter.isupper():
        digit = digit / (ord(first_letter) - 64)
    else:
        digit = digit * (ord(first_letter) - 96)

    if last_letter.isupper():
        digit = digit - (ord(last_letter) - 64)
    else:
        digit = digit + (ord(last_letter) - 96)
    return digit


def main():
    total_sum = 0
    string_sequence = input().split()
    for some_string in string_sequence:
        result = processing_the_string(some_string)
        total_sum += result

    print(f"{total_sum:.2f}")


main()