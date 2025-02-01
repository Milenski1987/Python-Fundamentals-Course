def palindrome(list_numbers: list) -> list:
    elements_result = []
    for element in list_numbers:
        if element == element[::-1]:
            elements_result.append("True")
        else:
            elements_result.append("False")
    return elements_result


list_of_integers_as_strings = input().split(", ")
result = palindrome(list_of_integers_as_strings)

print("\n".join(result))