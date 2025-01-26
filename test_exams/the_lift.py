waiting_people = int(input())
lift_wagons = [int(number) for number in input().split()]

wagon_capacity = 4

for index in range(len(lift_wagons)):
    if lift_wagons[index] < wagon_capacity and waiting_people > 0:
        free_space = wagon_capacity - lift_wagons[index]
        if waiting_people > free_space:
            lift_wagons[index] += free_space
            waiting_people -= free_space
        else:
            lift_wagons[index] += waiting_people
            waiting_people = 0

if waiting_people == 0 and lift_wagons.count(wagon_capacity) != len(lift_wagons):
    print("The lift has empty spots!")

elif waiting_people > 0 and lift_wagons.count(wagon_capacity) == len(lift_wagons):
    print(f"There isn't enough space! {waiting_people} people in a queue!")

print(*lift_wagons,sep=" ")