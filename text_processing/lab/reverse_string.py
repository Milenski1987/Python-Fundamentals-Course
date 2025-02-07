def reverse_string(some_string: str) -> str:
    reversed_some_string = some_string[::-1]
    return reversed_some_string


def main():
    while True:
        current_string = input()

        if current_string == "end":
            break

        reversed_current_string = reverse_string(current_string)
        print(f"{current_string} = {reversed_current_string}")


main()