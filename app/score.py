from app.gui import Gui

gui = Gui()
class Score:
    def __init__(self, storage):
        self.storage = storage

    def type_points_of_players(self, game_round):
        for key in self.storage:
            #round_points = gui1.enterbox(msg=f'Количество очков в раунде №{game_round} у {key}', title='Очки в раунде')
            round_points = gui.input_window(window_title='Очки в раунде',
                                               window_text=f'Количество очков в раунде №{game_round} у {key}')
            while not round_points.isdigit():
                round_points = gui.input_window(window_title='Очки в раунде',
                                                  window_text=f'Значение должно быть числом!'
                                                              f'\nКоличество очков в раунде №{game_round} у {key}')
            self.storage.update({key: int(round_points) + int(self.storage[key])})
        return self.storage

    def show_points_and_round(self, game_round):
        round_points = ''
        for key, value in self.storage.items():
            round_points += f'{key} - {value}\n'
        gui.show_message_window(window_title='Конец раунда',
                                window_text=f'Счет на конец раунда №{game_round}\n{round_points}')

    def show_winner(self, max_point):
        stop_point = int(sorted(self.storage.values())[-1])
        winners = []
        if stop_point >= max_point:
            for key in self.storage:
                if self.storage[key] == stop_point:
                    winners.append(key)
            gui.show_message_window(window_title='Победа',
                                    window_text=f'Поздравим победителя(ей) {", ".join(winners)} '
                                           f'с набором нужного количества очков - {max_point}')
        return stop_point
