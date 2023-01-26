import score


storage = dict()
player_list = []
stop_point = 0


while True:
    max_point = score.type_max_point()
    players_number = score.type_players_number()


    """
    print('Введите количество игроков:')
    players_number = input()
"""
    for i in range(1, int(players_number) + 1):
        print(f'Введите имя игрока {i}:')
        player_name = input()
        player_list.append(player_name)

    point_storage = score.create_player_and_points_storage(storage, players_number, player_list)
    points_adding = score.scoring

    while int(stop_point) < int(max_point()):
        points_adding(storage)
        stop_point = sorted(storage.values())[-1]
        if int(stop_point) >= int(max_point):
            winner = max(storage, key=storage.get)
            print(f'Игра закончена! Поздравим победителя - {winner}\n{storage}')
