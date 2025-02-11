def cheating(count: int, elements: list[str]) -> list[str]:
    element_to_add = f"-{count}a"
    index_to_add = len(elements) // 2
    elements.insert(index_to_add, element_to_add)
    elements.insert(index_to_add, element_to_add)
    print("Invalid input! Adding additional elements to the board")
    return elements


def memory_game(elements: list[str]) -> tuple:
    counter = 0
    while True:
        command = input()

        if command == "end":
            return "Sorry you lose :(", elements

        counter += 1

        first_index = int(command.split()[0])
        second_index = int(command.split()[1])

        if first_index == second_index or first_index not in range(len(elements)) or second_index not in range(len(elements)):
            elements = cheating(counter, elements)
            continue

        if elements[first_index] == elements[second_index]:
            print(f"Congrats! You have found matching elements - {elements[first_index]}!")
            if first_index > second_index:
                elements.pop(first_index)
                elements.pop(second_index)
            elif first_index < second_index:
                elements.pop(second_index)
                elements.pop(first_index)
        else:
            print("Try again!")

        if not elements:
            return f"You have won in {counter} turns!", elements



def main():
    element_sequence = input().split()
    message, element_sequence = memory_game(element_sequence)
    print(message)
    if element_sequence:
        print(" ".join(element_sequence))


main()