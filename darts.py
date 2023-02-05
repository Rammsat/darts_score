import score
import players
import statistic


rounds = 0

while True:
    max_point = players.type_max_point()
    players_number = players.type_players_number()
    player_list = players.create_player_list(players_number)

    point_storage = score.create_player_and_points_storage(players_number, player_list)

    while True:
        adding_points = score.scoring(point_storage)
        rounds += 1
        score.show_points_and_round(rounds, point_storage)
        stop_game_points = score.show_winner(max_point, point_storage)
        if stop_game_points >= max_point:
            break

    connection = statistic.create_connection_to_db()
    update_number_of_games = statistic.update_statistics(connection, adding_points)
