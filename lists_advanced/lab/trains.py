def add(wagons: list, number_of_people: int) -> list:
    wagons[-1] += number_of_people
    return wagons


def insert(wagons: list, current_index: int, number_of_people: int) -> list:
    wagons[current_index] += number_of_people
    return wagons


def leave(wagons: list, current_index: int, number_of_people: int) -> list:
    wagons[current_index] -= number_of_people
    return wagons


def main():
    train = [0] * int(input())

    while True:
        command = input()

        if command == "End":
            print(train)
            break

        current_command = command.split()
        action = current_command[0]

        if action == "add":
            people = int(current_command[1])
            train = add(train, people)

        elif action == "insert":
            index = int(current_command[1])
            people = int(current_command[2])
            train = insert(train, index, people)

        elif action == "leave":
            index = int(current_command[1])
            people = int(current_command[2])
            train = leave(train, index, people)


main()
