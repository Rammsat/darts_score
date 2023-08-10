from app.gui import Gui

gui = Gui()
class GamePreparation:
    def __init__(self):
        self.player_list = None
        self.players_number = None

    def type_max_point(self):
        while True:
            try:
                max_point = int(gui.input_window(window_title='Очки', window_text='Введите максимальное количество очков'))
                break
            except ValueError:
                gui.pop_up()
        return max_point

    def type_players_number(self):
        while True:
            try:
                self.players_number = int(gui.input_window(window_title='Количество игроков',
                                                           window_text='Введите количество игроков'))
                #int(gui.enterbox(msg='Введите количество игроков', title='Игроки'))
                break
            except ValueError:
                gui.pop_up()
                #gui.msgbox(msg='Значение должно быть числом!', title='Ошибка')

    def type_players_names(self):
        self.player_list = []
        for i in range(1, self.players_number + 1):
            player_name = gui.input_window(window_title='Имя', window_text='Введите имя игрока')
            self.player_list.append(player_name)
        return self.player_list

    def create_player_and_points_storage(self):
        storage = dict()
        for j in range(self.players_number):
            dict_of_player = {self.player_list[j]: 0}
            storage.update(dict_of_player)
        return storage
