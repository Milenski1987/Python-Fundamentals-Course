def find_and_remove_element(distances: list) -> tuple:
    index = int(input())
    removed_element = 0
    if index < 0:
        removed_element = distances.pop(0)
        distances.insert(0, distances[-1])

    elif index > len(distances) - 1:
        removed_element = distances.pop(-1)
        distances.append(distances[0])
    else:
        removed_element = distances.pop(index)

    return distances, removed_element


def update_values_of_elements(distances: list, removed_element: int) -> list:
    for index in range(len(distances)):
        if distances[index] <= removed_element:
            distances[index] += removed_element
        elif distances[index] > removed_element:
            distances[index] -= removed_element
    return distances


pokemon_distance = [int(number) for number in input().split()]
total_removed_elements = 0

while True:
    pokemon_distance, current_removed_element = find_and_remove_element(pokemon_distance)
    total_removed_elements += current_removed_element

    pokemon_distance = update_values_of_elements(pokemon_distance, current_removed_element)

    if not pokemon_distance:
        print(total_removed_elements)
        break
