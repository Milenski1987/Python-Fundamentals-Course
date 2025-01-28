initial_energy = 100
initial_coins = 100

working_day_events = input().split("|")
for event in working_day_events:
    current_event, value = event.split("-")
    value = int(value)

    if current_event == "rest":
        current_energy = initial_energy
        initial_energy += value
        if initial_energy > 100:
            initial_energy = 100
        diff_energy = initial_energy - current_energy
        print(f"You gained {diff_energy} energy.\nCurrent energy: {initial_energy}.")

    elif current_event == "order":
        if initial_energy >= 30:
            initial_coins += value
            initial_energy -= 30
            print(f"You earned {value} coins.")
        else:
            initial_energy += 50
            print("You had to rest!")

    else:
        if initial_coins >= value:
            initial_coins -= value
            print(f"You bought {current_event}.")
        else:
            print(f"Closed! Cannot afford {current_event}.")
            break

else:
    print("Day completed!")
    print(f"Coins: {initial_coins}\nEnergy: {initial_energy}")