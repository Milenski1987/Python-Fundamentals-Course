food_quantity = float(input())
hay_quantity = float(input())
cover_quantity = float(input())
pig_weight = float(input())

for day in range(1, 31):
    food_quantity -= 0.300

    if day % 2 == 0:
        hay_quantity -= food_quantity * 0.05

    if day % 3 == 0:
        cover_quantity -= pig_weight / 3

    if food_quantity <= 0 or hay_quantity <= 0 or cover_quantity <= 0:
        print("Merry must go to the pet store!")
        break

else:
    print(f"Everything is fine! Puppy is happy! Food: {food_quantity:.2f}, Hay: {hay_quantity:.2f}, Cover: {cover_quantity:.2f}.")