sheep_queue = input().split(", ")
sheep_count = 0

for position in range(len(sheep_queue) - 1, -1, -1):
    if sheep_queue[position] == "wolf" and sheep_count == 0:
        print("Please go away and stop eating my sheep")
        break
    elif sheep_queue[position] == "wolf":
        print(f"Oi! Sheep number {sheep_count}! You are about to be eaten by a wolf!")
        break
    else:
        sheep_count += 1
