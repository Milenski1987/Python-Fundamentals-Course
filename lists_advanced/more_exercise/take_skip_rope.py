def create_digits_non_digits_lists(current_string: str) -> list:
    current_digits_list = []
    current_non_digits_list = []

    for character in current_string:
        if character.isdigit():
            current_digits_list.append(character)
        else:
            current_non_digits_list.append(character)
    return current_digits_list, current_non_digits_list


def create_take_skip_lists(list_of_digits:list,) -> list:
    current_take_list = []
    current_skip_list = []
    for index in range(len(list_of_digits)):
        if index % 2 == 0:
            current_take_list.append(list_of_digits[index])
        else:
            current_skip_list.append(list_of_digits[index])
    return current_take_list, current_skip_list


def create_final_string(to_take_list: list, to_skip_list: list, list_of_non_digits: list) -> str:
    current_string = ""
    for i in range(len(to_take_list)):
        take_chars = int(to_take_list[i])
        skip_chars = int(to_skip_list[i]) + take_chars
        current_string += "".join(list_of_non_digits[:take_chars])
        list_of_non_digits = list_of_non_digits[skip_chars:]
    return current_string

initial_string = input()
digits_list, non_digits_list = create_digits_non_digits_lists(initial_string)
take_list, skip_list = create_take_skip_lists(digits_list)
result_string = create_final_string(take_list, skip_list, non_digits_list)

print(result_string)