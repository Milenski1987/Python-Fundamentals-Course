def update_phone_book(phonebook: dict, name: str, number: str) -> dict:
    if name not in phonebook:
        phonebook[name] = ""
    phonebook[name] = number
    return phonebook


def search_for_contact(phonebook: dict, current_name: str) -> str:
    if current_name in phonebook:
        return f"{current_name} -> {phonebook[current_name]}"
    else:
        return f"Contact {current_name} does not exist."


def main():
    phone_book = {}

    command = input()
    while "-" in command:
        current_name, current_phone = command.split("-")
        phone_book = update_phone_book(phone_book, current_name, current_phone)

        command = input()

    number_of_searches = int(command)

    for _ in range(number_of_searches):
        name = input()
        result = search_for_contact(phone_book, name)
        print(result)


main()