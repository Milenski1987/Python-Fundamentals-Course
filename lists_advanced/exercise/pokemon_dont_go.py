pokemon_distance = [int(number) for number in input().split()]
total_removed_elements = 0

while True:
    index = int(input())

    removed_element = 0
    if index < 0:
        removed_element = pokemon_distance.pop(0)
        pokemon_distance.insert(0, pokemon_distance[-1])

    elif index > len(pokemon_distance) - 1:
        removed_element = pokemon_distance.pop(-1)
        pokemon_distance.append(pokemon_distance[0])
    else:
        removed_element = pokemon_distance.pop(index)

    total_removed_elements += removed_element

    for idx in range(len(pokemon_distance)):
        if pokemon_distance[idx] <= removed_element:
            pokemon_distance[idx] += removed_element
        elif pokemon_distance[idx] > removed_element:
            pokemon_distance[idx] -= removed_element

    if not pokemon_distance:
        print(total_removed_elements)
        break
