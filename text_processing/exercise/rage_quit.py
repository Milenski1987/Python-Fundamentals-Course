def create_rage_quit(command_string: str) -> tuple:
    rage_quit_string = ""
    unique_symbols = []

    working_string = ""
    multiplier = ""
    for index in range(len(command_string)):
        if command_string[index].isdigit():
            multiplier += command_string[index]
            if index != len(command_string) - 1:
                if command_string[index + 1].isdigit():
                    multiplier += command_string[index + 1]
            if working_string:
                rage_quit_string += working_string * int(multiplier)
            working_string = ""
            multiplier = ""

        elif command_string[index].isalpha():
            working_string += command_string[index].upper()
            if command_string[index].lower() not in unique_symbols:
                unique_symbols.append(command_string[index].lower())

        else:
            working_string += command_string[index]
            if command_string[index] not in unique_symbols:
                unique_symbols.append(command_string[index])

    return rage_quit_string, len(unique_symbols)

def main():
    some_string = input()
    final_string, unique_symbols_count = create_rage_quit(some_string)

    print(f"Unique symbols used: {len(unique_symbols_count)}")
    print(final_string)


main()