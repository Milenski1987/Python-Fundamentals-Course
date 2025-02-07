def check_ticket(current_ticket: str, symbols_of_win: list) -> str:
    if check_for_validity(current_ticket):
        symbols_count, symbol_type = check_for_winning_symbols(current_ticket, symbols_of_win)

        if 6 <= symbols_count < 10:
            return f'ticket "{current_ticket}" - {symbols_count}{symbol_type}'

        elif symbols_count == 10:
            return  f'ticket "{current_ticket}" - {symbols_count}{symbol_type} Jackpot!'

        else:
            return f'ticket "{current_ticket}" - no match'

    return "invalid ticket"


def check_for_validity(current_ticket: str) -> bool:
    if len(current_ticket) == 20:
        return True
    return False


def check_for_winning_symbols(current_ticket: str, symbols_of_win: list) -> tuple:
    first_half = current_ticket[:10]
    second_half = current_ticket[10:]
    matched_symbols = 0
    matched_winning_symbol = ""

    for symbol in symbols_of_win:
        if 6 * symbol in first_half and 6 * symbol in second_half:
            matched_symbols += count_winning_symbols(symbol, first_half, second_half)
            matched_winning_symbol = symbol
            return matched_symbols, matched_winning_symbol
    return matched_symbols, matched_winning_symbol


def count_winning_symbols(current_symbol: str, ticket_first_half: str, ticket_second_half: str) -> int:
    counted_symbols = 6
    for number in range(7, 11):
        if number * current_symbol in ticket_first_half and number * current_symbol in ticket_second_half:
            counted_symbols = number
    return counted_symbols


def main():
    tickets = input().replace(" ", "" ).split(",")
    winning_symbols = ["@", "#", "$", "^"]
    for ticket in tickets:
        result = check_ticket(ticket, winning_symbols)
        print(result)


main()