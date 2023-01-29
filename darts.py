import score
import players


rounds = 0

while True:
    max_point = players.type_max_point()
    players_number = players.type_players_number()
    player_list = players.create_player_list(players_number)

    point_storage = score.create_player_and_points_storage(players_number, player_list)
    adding_points = score.scoring
    show_end_of_round = score.show_points_and_round

    while True:
        adding_points(point_storage)
        rounds += 1
        show_end_of_round(rounds, point_storage)
        stop_game_points = score.show_winner(max_point, point_storage)
        if stop_game_points >= max_point:
            break
