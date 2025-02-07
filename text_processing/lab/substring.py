def remove_substring(some_substring: str, some_string: str) -> str:
    while some_substring in some_string:
        some_string = some_string.replace(some_substring, "")
    return some_string


def main():
    substring = input()
    current_string = input()

    result_string = remove_substring(substring, current_string)
    print(result_string)


main()