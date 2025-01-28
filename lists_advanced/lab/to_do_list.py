to_do_list = [0] * 10

while True:
    command = input()

    if command == "End":
        break

    current_command = command.split("-")
    importance = int(current_command[0]) - 1
    note = current_command[1]

    to_do_list.pop(importance)
    to_do_list.insert(importance, note)

result = [note for note in to_do_list if note != 0]
print(result)