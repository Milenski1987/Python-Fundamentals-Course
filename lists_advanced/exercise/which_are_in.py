first_string_sequence = input().split(", ")
second_string_sequence = input().split(", ")
result = []

for element in first_string_sequence:
    for some_element in second_string_sequence:
        if element in some_element and element not in result:
            result.append(element)
print(result)