class GamePreparation:
    def __init__(self):
        self.player_list = None
        self.players_number = None

    def type_max_point(self):
        while True:
            try:
                max_point = int(input('Введите максимальное количество очков: '))
                break
            except ValueError:
                print('Значение должно быть числом!')
        return max_point

    def type_players_number(self):
        while True:
            try:
                self.players_number = int(input('Введите количество игроков: '))
                break
            except ValueError:
                print('Значение должно быть числом!')

    def type_players_names(self):
        self.player_list = []
        for i in range(1, self.players_number + 1):
            player_name = input(f'Введите имя игрока {i}: ')
            self.player_list.append(player_name)
        return self.player_list

    def create_player_and_points_storage(self):
        storage = dict()
        for j in range(self.players_number):
            dict_of_player = {self.player_list[j]: 0}
            storage.update(dict_of_player)
        return storage
