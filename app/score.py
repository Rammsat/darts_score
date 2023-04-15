class Score:
    def __init__(self, storage):
        self.storage = storage

    def type_points_of_players(self, game_round):
        for key in self.storage:
            round_points = input(f'Количество очков в раунде №{game_round} у {key}: ')
            while not round_points.isdigit():
                round_points = input(f'Значение должно быть числом!\nКоличество очков в раунде №{game_round} у {key}: ')
            self.storage.update({key: int(round_points) + int(self.storage[key])})
        return self.storage

    def show_points_and_round(self, game_round):
        print(f'Счет на конец раунда №{game_round}:')
        for key, value in self.storage.items():
            print(f'{key} - {value}')

    def show_winner(self, max_point):
        stop_point = int(sorted(self.storage.values())[-1])
        winners = list()
        if stop_point >= max_point:
            for key in self.storage:
                if self.storage[key] == stop_point:
                    winners.append(key)
        print(f'Поздравим победителя(ей) {", ".join(winners)} с набором нужного количества очков - {max_point}')
        return stop_point
