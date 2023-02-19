def create_player_and_points_storage(players_number, player_list):
    storage = dict()
    for j in range(players_number):
        dict_of_player = {player_list[j]: 0}
        storage.update(dict_of_player)
    return storage


def scoring(storage: dict, game_round):
    for key in storage:
        round_points = input(f'Количество очков в раунде №{game_round} у {key}: ')
        while not round_points.isdigit():
            round_points = input(f'Значение должно быть числом!\nКоличество очков в раунде №{game_round} у {key}: ')
        storage.update({key: int(round_points) + int(storage[key])})
    return storage


def show_points_and_round(rounds, storage: dict):
    print(f'Счет на конец раунда №{rounds}:')
    for key, value in storage.items():
        print(f'{key} - {value}')


def show_winner(max_point, storage):
    stop_point = int(sorted(storage.values())[-1])
    winners = list()
    if stop_point >= max_point:
        for key in storage:
            if storage[key] == stop_point:
                winners.append(key)
        print(f'Поздравим победителя(ей) {", ".join(winners)} с набором нужного количества очков - {max_point}')
    return stop_point
