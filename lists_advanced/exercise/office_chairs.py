number_of_rooms = int(input())
free_chairs = 0
chairs_for_everyone = True

for room in range(1, number_of_rooms + 1):
    status = input().split()
    available_chairs = len(status[0])
    people_in_room = int(status[1])

    if available_chairs < people_in_room:
        needed_chairs = people_in_room - available_chairs
        chairs_for_everyone = False
        print(f"{needed_chairs} more chairs needed in room {room}")

    else:
        free_chairs += available_chairs - people_in_room

if chairs_for_everyone:
    print(f"Game On, {free_chairs} free chairs left")