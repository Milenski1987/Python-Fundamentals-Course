def loading(lift: list, people: int, capacity: int) -> tuple:
    for wagon in range(len(lift)):
        if lift[wagon] < capacity:
            empty_spots = capacity - lift[wagon]
            if people > empty_spots:
                lift[wagon] += empty_spots
                people -= empty_spots
            else:
                lift[wagon] += people
                people = 0
    return lift, people


def main():
    wagon_capacity = 4
    people_waiting = int(input())
    lift_wagons = [int(number) for number in input().split()]

    lift_wagons, people_waiting = loading(lift_wagons, people_waiting, wagon_capacity)

    result = ""
    lift_wagons_as_strings = [str(wagon) for wagon in lift_wagons]
    if people_waiting == 0 and lift_wagons.count(wagon_capacity) < len(lift_wagons):
        result = f"The lift has empty spots!\n{' '.join(lift_wagons_as_strings)}"
    elif people_waiting > 0 and lift_wagons.count(wagon_capacity) == len(lift_wagons):
        result = f"There isn't enough space! {people_waiting} people in a queue!\n{' '.join(lift_wagons_as_strings)}"
    else:
        result = f"{' '.join(lift_wagons_as_strings)}"
    print(result)


main()