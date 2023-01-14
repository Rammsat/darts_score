print('Привет! До скольки очков будет длиться игра?')
max_point = input()
rounds = 1
storage = dict()
player_list = []

print('Введите количество игроков:')
players_number = input()


for i in range(1, int(players_number) + 1):
    print(f'Введите имя игрока {i}:')
    player_name = input()
    player_list.append(player_name)


def player_storage(some_dict):
    for j in range(int(players_number)):
        dict_of_player = {player_list[j]: 0}
        some_dict.update(dict_of_player)
    return some_dict


player_storage(storage)


def scoring():
    for key, value in storage.items():
        print(f'Сколько очков набрал {key}?')
        round_points = input()
        storage[value] = storage[value] + int(round_points)
    return storage


print(scoring())


