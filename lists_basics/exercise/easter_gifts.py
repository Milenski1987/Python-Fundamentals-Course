gifts = input().split()

while True:
    command = input()

    if command == "No Money":
        break

    current_command = command.split()
    action = current_command[0]
    gift = current_command[1]

    if action == "OutOfStock":
        for i in range(len(gifts)):
            if gifts[i] == gift:
                gifts[i] = None

    elif action == "Required":
        index = int(current_command[2])
        if index in range(len(gifts)):
            gifts[index] = gift

    elif action == "JustInCase":
        gifts.pop()
        gifts.append(gift)

for index in range(len(gifts) - 1, -1 , -1):
    if gifts[index] is None:
        gifts.pop(index)

print(" ".join(gifts))