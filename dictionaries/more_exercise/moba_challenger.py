def create_players_pool(players_data: dict, current_player: str, current_position: str, current_skill: int) -> dict:
    if current_player not in players_data:
        players_data[current_player] = {}
        players_data[current_player][current_position] = current_skill
    if current_position not in players_data[current_player]:
        players_data[current_player][current_position] = current_skill
    if current_skill > players_data[current_player][current_position]:
        players_data[current_player][current_position] = current_skill
    return players_data


def duel(players_data: dict, player1: str, player2: str) -> dict:
    have_duel = False
    if player1 in players_data and player2 in players_data:
        for role in players_data[player1].keys():
            if role in players_data[player2].keys():
                have_duel = True
                break
        if have_duel:
            first_player_skills = calculate_total_skills(players_data, player1)
            second_player_skills = calculate_total_skills(players_data, player2)
            if first_player_skills > second_player_skills:
                del players_data[player2]
            elif first_player_skills < second_player_skills:
                del players_data[player1]
    return players_data


def calculate_total_skills(players_data: dict, player: str) -> int:
    player_total_skills = 0
    for skill in players_data[player].values():
        player_total_skills += skill
    return player_total_skills


def main():
    players = {}
    players_total_skill = {}

    while True:
        command = input()

        if command == "Season end":
            break

        elif "->" in command:
            current_command = command.split(" -> ")
            player = current_command[0]
            position = current_command[1]
            skill = int(current_command[2])
            players = create_players_pool(players, player, position, skill)

        else:
            current_command = command.split(" vs ")
            first_player = current_command[0]
            second_player = current_command[1]
            players = duel(players, first_player, second_player)

    for player in players.keys():
        total_skills = calculate_total_skills(players, player)
        players_total_skill[player] = total_skills

    players_total_skill = dict(sorted(players_total_skill.items(), key=lambda x: (-x[1], x[0])))
    for player, total_skill in players_total_skill.items():
        print(f"{player}: {total_skill} skill")
        players[player] = dict(sorted(players[player].items(), key=lambda x: (-x[1], x[0])))
        for position, skill in players[player].items():
            print(f"- {position} <::> {skill}")


main()