import score


rounds = 0

while True:
    max_point = score.type_max_point()
    players_number = score.type_players_number()
    player_list = score.create_player_list(players_number)

    point_storage = score.create_player_and_points_storage(players_number, player_list)
    adding_points = score.scoring
    show_end_of_round = score.show_points_and_round

    while True:
        adding_points(point_storage)
        rounds += 1
        show_end_of_round(rounds, point_storage)
        stop_game = score.show_winner(max_point, point_storage)
        if stop_game >= max_point:
            break
