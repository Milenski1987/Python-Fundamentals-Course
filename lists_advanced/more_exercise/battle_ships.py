def current_attack(field: list, attacked: list, rows: int) -> int:
    current_destroyed_ships = 0
    current_row_index , current_column_index = attacked.split("-")
    current_row_index = int(current_row_index)
    current_column_index = int(current_column_index)

    if current_row_index in range(rows) and current_column_index in range(len(field[0])):
        if field[current_row_index][current_column_index] > 0:
            field[current_row_index][current_column_index] -= 1
            if field[current_row_index][current_column_index] == 0:
                current_destroyed_ships += 1

    return current_destroyed_ships


def create_battlefield(rows: int) -> list:
    field = []
    for _ in range(rows):
        row = [int(number) for number in input().split()]
        field.append(row)
    return field


def main():
    rows_on_field = int(input())
    battlefield = create_battlefield(rows_on_field)
    attacked_squares = input().split()

    destroyed_ships = 0

    for attack in attacked_squares:
        destroyed_ships += current_attack(battlefield, attack, rows_on_field)

    print(destroyed_ships)


main()