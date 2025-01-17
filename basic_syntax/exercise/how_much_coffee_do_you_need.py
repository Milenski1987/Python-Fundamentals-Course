coffee_counter = 0

while True:
    command = input()

    if command == "END":
        break

    if command.lower() == "coding" or command.lower() == "dog" or command.lower() == "cat" or command.lower() == "movie":
        if command.islower():
            coffee_counter += 1
        elif command.isupper():
            coffee_counter += 2

if coffee_counter > 5:
    print("You need extra sleep")
else:
    print(coffee_counter)