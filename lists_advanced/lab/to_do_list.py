def list_creation_and_edit() -> list:
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

    return to_do_list


final_list = list_creation_and_edit()
result = [note for note in final_list if note != 0]
print(result)



# Advance solution:
#
# def process_todo_notes():
#     todo_notes = []
#     while True:
#         note = input()
#         if note == "End":
#             break
#         todo_notes.append(note)
#
#     sorted_notes = sorted(todo_notes, key=lambda x: int(x.split("-")[0]))
#     string_sorted = [note.split("-")[1] for note in sorted_notes]
#     return string_sorted
#
#
# result = process_todo_notes()
# print(result)
