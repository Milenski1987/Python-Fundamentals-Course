def bakery_data(bakery_foods: dict, bakery_information: list) -> dict:
    for index in range(0, len(bakery_information), 2):
        bakery_foods[bakery_information[index]] = int(bakery_information[index + 1])
    return bakery_foods

food_data = input().split()
foods = {}
foods = bakery_data(foods, food_data)

print(foods)
