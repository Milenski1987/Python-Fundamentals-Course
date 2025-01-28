people_in_circle = input().split()
kill_number = int(input())

executed_people = []
index_to_kill = 0
counter = 0

while True:
    counter += 1

    if counter % kill_number == 0:
        executed_people.append(people_in_circle[index_to_kill])
        people_in_circle.pop(index_to_kill)

    else:
        index_to_kill += 1

    if index_to_kill >= len(people_in_circle):
        index_to_kill = 0

    if not people_in_circle:
        break

result = ""
for i in range(len(executed_people)):
    if i == len(executed_people) - 1:
        result += executed_people[i]
    else:
        result += executed_people[i] + ","

print(f"[{result}]")