number_of_lines = int(input())
open_bracket = False
close_bracket = False


for _ in range(number_of_lines):
    symbol = input()

    if symbol == "(":
        if open_bracket and not close_bracket:
            break
        open_bracket = True
    elif symbol == ")":
        if open_bracket:
            close_bracket = True
        else:
            break

if open_bracket and close_bracket:
    print("BALANCED")
else:
    print("UNBALANCED")