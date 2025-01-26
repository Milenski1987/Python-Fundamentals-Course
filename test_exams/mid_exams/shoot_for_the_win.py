targets = [int(number) for number in input().split()]

while True:
    command = input()

    if command == "End":
        final_targets = [str(target) for target in targets]
        print(f"Shot targets: {targets.count(-1)} -> {' '.join(final_targets)}")
        break

    index = int(command)

    if index not in range(len(targets)):
        continue

    if targets[index] != -1:
        target_to_shot = targets[index]
        for i in range(len(targets)):
            if targets[i] > target_to_shot and targets[i] != -1 and i != index:
                targets[i] -= target_to_shot
            elif targets[i] <= target_to_shot and targets[i] != -1 and i != index:
                targets[i] += target_to_shot

        targets[index] = -1