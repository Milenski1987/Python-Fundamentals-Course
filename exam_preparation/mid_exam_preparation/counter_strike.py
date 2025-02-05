def reach_enemy(current_energy: int, current_distance: int) -> tuple:
    score = 0
    if current_distance > current_energy:
        score = 0
    else:
        current_energy -= current_distance
        score = 1
    return score, current_energy


def main():
    energy = int(input())
    win_count = 0

    while True:
        command = input()
        if command == "End of battle":
            print(f"Won battles: {win_count}. Energy left: {energy}")
            break

        distance = int(command)

        result, energy = reach_enemy(energy, distance)
        win_count += result

        if result == 0:
            print(f"Not enough energy! Game ends with {win_count} won battles and {energy} energy")
            break

        if win_count % 3 == 0:
            energy += win_count


main()