def create_player_and_points_storage(storage, players_number, player_list):
    for j in range(int(players_number)):
        dict_of_player = {player_list[j]: 0}
        storage.update(dict_of_player)
    return storage


def scoring(storage):
    for key in storage:
        print(f'Сколько очков набрал {key}?')
        round_points = input()
        storage.update({key: int(round_points) + int(storage[key])})
    print(f'Счет на конец раунда: \n{storage}')


def type_max_point():
    print('До скольки очков будет длиться игра?')
    max_point = input()
    if max_point.isalpha():
        print('Максимальное число очков не может быть не числом!')
        type_max_point()
    return max_point


def type_players_number():
    print('Введите количество игроков:')
    players_number = input()
    if players_number.isalpha():
        print('Количество игроков должно быть числом!')
        type_players_number()
    return players_number

"""
def create_player_list(players_number):
    for i in range(1, int(players_number) + 1):
        print(f'Введите имя игрока {i}:')
        player_name = input()
        player_list.append(player_name)
"""