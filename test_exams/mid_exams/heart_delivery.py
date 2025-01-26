neighborhood = [int(number) for number in input().split("@")]


index = 0
while True:
    command = input()

    if command == "Love!":
        print(f"Cupid's last position was {index}.")
        break

    current_command = command.split()
    length = int(current_command[1])

    if index + length >= len(neighborhood):
        index = 0
    else:
        index += length

    if neighborhood[index] == 0:
        print(f"Place {index} already had Valentine's day.")

    else:
        neighborhood[index] -= 2
        if neighborhood[index] == 0:
            print(f"Place {index} has Valentine's day.")

result = ""
if neighborhood.count(0) == len(neighborhood):
    result = "Mission was successful."
else:
    failed_houses = len(neighborhood) - neighborhood.count(0)
    result = f"Cupid has failed {failed_houses} places."

print(result)