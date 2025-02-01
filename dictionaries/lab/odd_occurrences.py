def create_elements_dictionary(elements_result: dict, elements_data: list) -> dict:
    for element in elements_data:
        if element.lower() not in elements_result:
            elements_result[element.lower()] = 0
        elements_result[element.lower()] += 1
    return elements_result

def get_results(elements_result: dict) -> list:
    result = []
    for element, occurrence in elements_result.items():
        if occurrence % 2 != 0:
            result.append(element)
    return result


def main():
    elements_list = input().split()
    elements_dictionary = {}

    elements_dictionary = create_elements_dictionary(elements_dictionary, elements_list)
    final_result = get_results(elements_dictionary)

    if final_result:
        print(" ".join(final_result))


main()