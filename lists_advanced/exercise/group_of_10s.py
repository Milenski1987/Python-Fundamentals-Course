from math import ceil


initial_sequence = [int(number) for number in input().split(", ")]

number_of_groups = ceil(max(initial_sequence) / 10)

group_of = 10
for _ in range(number_of_groups):
    working_list = []
    for index in range(len(initial_sequence) - 1, -1, -1):
        if initial_sequence[index] <= group_of:
            found = initial_sequence.pop(index)
            working_list.append(found)

    working_list.reverse()
    print(f"Group of {group_of}'s: {working_list}")
    group_of += 10