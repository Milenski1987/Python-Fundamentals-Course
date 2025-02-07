def repeat_string(sequence: list) -> str:
    result_string = ""
    for current_string in sequence:
        result_string += current_string * len(current_string)
    return result_string


def main():
    strings_sequence = input().split()

    result = repeat_string(strings_sequence)
    print(result)


main()