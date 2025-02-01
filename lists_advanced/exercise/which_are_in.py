def search_for_substrings(first_strings: list, second_strings: list) -> list:
    result_list = []
    for element in first_strings:
        for some_element in second_strings:
            if element in some_element and element not in result_list:
                result_list.append(element)
    return result_list


first_string_sequence = input().split(", ")
second_string_sequence = input().split(", ")
result = search_for_substrings(first_string_sequence, second_string_sequence)

print(result)