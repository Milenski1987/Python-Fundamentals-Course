food_data = input().split()
foods = {}

for index in range(0, len(food_data), 2):
    foods[food_data[index]] = int(food_data[index + 1])
print(foods)
