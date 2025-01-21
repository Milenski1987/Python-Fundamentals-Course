first_line = input().split()
second_line = input().split()
third_line = input().split()
first_column = list(first_line[0] + second_line[0] + third_line[0])
second_column = list(first_line[1] + second_line[1] + third_line[1])
third_column = list(first_line[2] + second_line[2] + third_line[2])
first_diagonal = list(first_column[0] + second_column[1] + third_column[2])
second_diagonal = list(first_column[2] + second_column[1] + third_column[0])

first_player_win = ["1", "1", "1"]
second_player_win = ["2", "2", "2"]

possible_win_lines = [first_line, second_line, third_line, first_column, second_column, third_column, first_diagonal,second_diagonal]


for element in possible_win_lines:
    if element == first_player_win:
        print("First player won")
        break
    elif element == second_player_win:
        print("Second player won")
        break

else:
    print("Draw!")