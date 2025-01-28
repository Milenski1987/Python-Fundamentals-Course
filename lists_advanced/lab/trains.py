def add(wagons, ppl):
    wagons[-1] += ppl
    return wagons


def insert(wagons, idx, ppl):
    wagons[idx] += ppl
    return wagons


def leave(wagons, idx, ppl):
    wagons[idx] -= ppl
    return wagons


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