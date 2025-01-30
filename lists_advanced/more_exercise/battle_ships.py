rows_on_field = int(input())
field = []
destroyed_ships = 0

for _ in range(rows_on_field):
    row = [int(number) for number in input().split()]
    field.append(row)

attacked_squares = input().split()

for attack in attacked_squares:
    current_attack = attack.split("-")
    row_index = int(current_attack[0])
    column_index = int(current_attack[1])

    if row_index in range(rows_on_field) and column_index in range(len(field[0])):
        if field[row_index][column_index] > 0:
            field[row_index][column_index] -= 1
            if field[row_index][column_index] == 0:
                destroyed_ships += 1

print(destroyed_ships)