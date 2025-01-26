elements = input().split()
moves_count = 0

while True:
    command = input()

    if command == "end":
        print("Sorry you lose :(")
        print(" ".join(elements))
        break

    moves_count += 1

    first_index, second_index = command.split()
    first_index = int(first_index)
    second_index = int(second_index)

    if first_index == second_index or first_index not in range(len(elements)) or second_index not in range(len(elements)):
        element_to_add = f"-{moves_count}a"
        elements.insert(len(elements) // 2, element_to_add)
        elements.insert(len(elements) // 2, element_to_add)
        print("Invalid input! Adding additional elements to the board")
        continue

    if elements[first_index] == elements[second_index]:
        print(f"Congrats! You have found matching elements - {elements[first_index]}!")

        if first_index > second_index:
            elements.pop(first_index)
            elements.pop(second_index)
        else:
            elements.pop(second_index)
            elements.pop(first_index)

    else:
        print("Try again!")

    if not elements:
        print(f"You have won in {moves_count} turns!")
        break
