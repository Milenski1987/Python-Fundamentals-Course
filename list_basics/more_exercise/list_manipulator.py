integers_list = [int(number) for number in input().split()]

while True:
    command = input()

    if command == "end":
        print(integers_list)
        break

    even_numbers = [number for number in integers_list if number % 2 == 0]
    odd_numbers = [number for number in integers_list if number % 2 != 0]

    current_command = command.split()
    action = current_command[0]

    if action == "exchange":
        index = int(current_command[1])
        if index not in range(len(integers_list)):
            print("Invalid index")
        else:
            integers_list = integers_list[index + 1:] + integers_list[:index + 1]

    elif action == "max":
        second_action = current_command[1]
        index = 0

        if second_action == "even" and even_numbers:
            index = (len(integers_list) - 1) - integers_list[::-1].index(max(even_numbers))

        elif second_action == "odd" and odd_numbers:
            index = (len(integers_list) - 1) - integers_list[::-1].index(max(odd_numbers))

        else :
            print("No matches")
            continue

        print(index)

    elif action == "min":
        second_action = current_command[1]
        index = 0

        if second_action == "even" and even_numbers:
            index = (len(integers_list) - 1) - integers_list[::-1].index(min(even_numbers))

        elif second_action == "odd" and odd_numbers:
            index = (len(integers_list) - 1) - integers_list[::-1].index(min(odd_numbers))

        else :
            print("No matches")
            continue

        print(index)

    elif action == "first":
        count = int(current_command[1])
        second_action = current_command[2]
        result = []

        if second_action == "even" and count <= len(integers_list):
            result = even_numbers[:count]

        elif second_action == "odd" and count <= len(integers_list):
            result = odd_numbers[:count]

        else:
            print("Invalid count")
            continue

        print(result)

    elif action == "last":
        count = int(current_command[1])
        second_action = current_command[2]
        result = []

        if second_action == "even" and count <= len(integers_list):
            result = even_numbers[-count:]

        elif second_action == "odd" and count <= len(integers_list):
            result = odd_numbers[-count:]

        else:
            print("Invalid count")
            continue

        print(result)