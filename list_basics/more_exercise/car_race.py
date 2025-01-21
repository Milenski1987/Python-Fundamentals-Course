numbers = [int(number) for number in input().split()]
half_race = len(numbers) // 2

first_car_time = numbers[:half_race]
second_car_time = numbers[half_race + 1:]

first_car = 0
second_car = 0

for time in first_car_time:
    if int(time) == 0:
        first_car -= first_car * 0.20
    else:
        first_car += int(time)

for index in range(len(second_car_time) - 1, -1, -1):
    if int(second_car_time[index]) == 0:
        second_car -= second_car * 0.20
    else:
        second_car += int(second_car_time[index])

winner = ""
win_time = 0
if first_car < second_car:
    winner = "left"
    win_time = first_car
elif first_car > second_car:
    winner = "right"
    win_time = second_car

print(f"The winner is {winner} with total time: {win_time:.1f}")