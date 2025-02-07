def replace_repeating(some_string: str) -> str:
    result_string = ""
    for character in some_string:
        if character not in result_string:
            result_string += character
        else:
            if character != result_string[-1]:
                result_string += character
    return result_string


def main():
    current_string = input()

    final_string = replace_repeating(current_string)
    print(final_string)


main()