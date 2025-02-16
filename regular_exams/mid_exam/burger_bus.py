def current_city(city_num: int) -> float:
    city_name = input()
    owner_income = float(input())
    owner_expenses = float(input())

    if city_num % 3 == 0 and city_num % 5 != 0:
        owner_expenses += owner_expenses * 0.50

    if city_num % 5 == 0:
        owner_income -= owner_income * 0.10

    city_profit = owner_income - owner_expenses
    print(f"In {city_name} Burger Bus earned {city_profit:.2f} leva.")
    return city_profit


def main():
    number_of_cities = int(input())

    total_profit = 0

    for city_number in range(1, number_of_cities + 1):
        total_profit += current_city(city_number)

    print(f"Burger Bus total profit: {total_profit:.2f} leva.")


main()