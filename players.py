def type_max_point():
    while True:
        try:
            max_point = int(input('Введите максимальное количество очков: '))
            break
        except ValueError:
            print('Значение должно быть числом!')
    return max_point


def type_players_number():
    while True:
        try:
            players_number = int(input('Введите количество игроков: '))
            break
        except ValueError:
            print('Значение должно быть числом!')
    return players_number


def create_player_list(players_number):
    player_list = []
    for i in range(1, players_number + 1):
        player_name = input(f'Введите имя игрока {i}: ')
        player_list.append(player_name)
    return player_list
