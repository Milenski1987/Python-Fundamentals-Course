array = [int(number) for number in input().split()]

while True:
    command = input()

    if command == "end":
        break

    current_command = command.split()
    action = current_command[0]

    if action == "swap":
        first_index = int(current_command[1])
        second_index = int(current_command[2])

        array[first_index], array[second_index] = array[second_index], array[first_index]

    elif action == "multiply":
        first_index = int(current_command[1])
        second_index = int(current_command[2])

        array[first_index] *= array[second_index]

    elif action == "decrease":
        for index in range(len(array)):
            array[index] -= 1

print(*array, sep=", ")