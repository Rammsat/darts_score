def type_max_point():
    while True:
        print('До скольки очков будет длиться игра?')
        max_point = input()
        if max_point.isdigit():
            return int(max_point)
        else:
            print('Максимальное число очков не может быть не числом!')


def type_players_number():
    while True:
        print('Введите количество игроков:')
        players_number = input()
        if players_number.isdigit():
            return int(players_number)
        else:
            print('Количество игроков должно быть числом!')


def create_player_list(players_number):
    player_list = []
    for i in range(1, players_number + 1):
        print(f'Введите имя игрока {i}:')
        player_name = input()
        player_list.append(player_name)
    return player_list