def pig_feed(food: float, hay: float, cover: float, weight: float) -> str:
    for day in range(1, 31):
        food -= 0.300
        if day % 2 == 0:
            hay -= food * 0.05
        if day % 3 == 0:
            cover -= weight / 3

        if round(food, 2) <= 0 or round(hay, 2) <= 0 or round(cover, 2) <= 0:
            return "Merry must go to the pet store!"

    return f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}."


def main():
    food_quantity = float(input())
    hay_quantity = float(input())
    cover_quantity = float(input())
    pig_weight = float(input())

    result = pig_feed(food_quantity, hay_quantity, cover_quantity, pig_weight)
    print(result)


main()