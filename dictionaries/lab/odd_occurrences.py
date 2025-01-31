elements_list = input().split()
elements_dictionary = {}

for element in elements_list:
    if element.lower() not in elements_dictionary:
        elements_dictionary[element.lower()] = 0
    elements_dictionary[element.lower()] += 1

for element, occurrence in elements_dictionary.items():
    if occurrence % 2 != 0:
        print(element, end=" ")