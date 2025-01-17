while True:
    command = input()

    if command == "End":
        break

    if command == "SoftUni":
        continue

    string = ""
    for character in command:
        string += character * 2

    print(string)