import os.path
import sqlite3
import pandas
from sqlite3 import Error


class DataBase:
    def __init__(self):
        pass

    def create_connection(self):
        path_db = os.path.abspath('darts.db')
        self.connection = None
        try:
            self.connection = sqlite3.connect(path_db)
        except Error as e:
            print(f"The error '{e}' occurred")
        self.cursor = self.connection.cursor()
        return self.cursor

    def insert_players(self, players_list):
        exist_names = f"SELECT name " \
                      f"FROM players"
        list_of_names = self.cursor.execute(exist_names).fetchall()

        clear_list_of_names = [item[0] for item in list_of_names]
        for name in players_list:
            if name not in clear_list_of_names:
                last_id_script =  f"SELECT id " \
                                  f"FROM players " \
                                  f"ORDER BY id DESC " \
                                  f"LIMIT 1"

                last_id = self.cursor.execute(last_id_script).fetchall()

                # Нужно, если БД пуста
                if not last_id:
                    last_id = 0
                else:
                    last_id = last_id[0][0]

                insert_in_players = f"INSERT INTO players (id,name) " \
                                    f"VALUES ('{last_id + 1}','{name}')"
                self.cursor.execute(insert_in_players)

                insert_in_statistic = f"INSERT INTO statistic (player_id, number_of_games,max_points_in_game, " \
                                      f"avg_points_per_game,all_points,first_places,second_places,third_places)" \
                                      f"VALUES ('{last_id + 1}', 0, 0, 0, 0, 0, 0, 0)"
                self.cursor.execute(insert_in_statistic)
                self.connection.commit()


    def update_statistics(self, storage: dict):

        sorted_storage = sorted(storage, key=storage.get, reverse=True)

        for name in sorted_storage:
            select_data = f"SELECT statistic.* " \
                      f"FROM statistic JOIN players ON" \
                      f" players.id = statistic.player_id "\
                      f"where name = '{name}'"
            db_data = self.cursor.execute(select_data).fetchall()

            games_number = db_data[0][1] + 1
            update_games = f"UPDATE statistic SET number_of_games = {games_number} WHERE player_id = " \
                       f"(SELECT player_id  FROM statistic JOIN players " \
                           f"ON players.id = statistic.player_id " \
                       f"WHERE players.name = '{name}')"
            self.cursor.execute(update_games)

            all_points = db_data[0][4] + storage[name]
            update_all_points = f"UPDATE statistic SET all_points = {all_points} WHERE player_id = " \
                            f"(SELECT player_id  FROM statistic JOIN players " \
                                f"ON players.id = statistic.player_id " \
                            f"WHERE players.name = '{name}')"
            self.cursor.execute(update_all_points)

            avg_points = all_points / games_number
            update_avg_points = f"UPDATE statistic SET avg_points_per_game = {avg_points} WHERE player_id = " \
                            f"(SELECT player_id  FROM statistic JOIN players " \
                                f"ON players.id = statistic.player_id " \
                            f"WHERE players.name = '{name}')"
            self.cursor.execute(update_avg_points)

            if db_data[0][2] < storage[name]:
                update_max_points = f"UPDATE statistic SET max_points_in_game = {storage[name]} WHERE player_id = " \
                                f"(SELECT player_id  FROM statistic JOIN players " \
                                    f"ON players.id = statistic.player_id " \
                                f"WHERE players.name = '{name}')"
                self.cursor.execute(update_max_points)

            # Обновлять данные по местам только, если игроков 3 или более
            if len(sorted_storage) >= 3:
                if name == sorted_storage[0]:
                    first_place = db_data[0][5] + 1
                    update_first_place = f"UPDATE statistic SET first_places = {first_place} WHERE player_id = " \
                                 f"(SELECT player_id  FROM statistic JOIN players " \
                                     f"ON players.id = statistic.player_id " \
                                 f"WHERE players.name = '{name}')"
                    self.cursor.execute(update_first_place)

                if name == sorted_storage[1]:
                    second_place = db_data[0][6] + 1
                    update_second_place = f"UPDATE statistic SET second_places = {second_place} WHERE player_id = " \
                                  f"(SELECT player_id  FROM statistic JOIN players " \
                                      f"ON players.id = statistic.player_id " \
                                  f"WHERE players.name = '{name}')"
                    self.cursor.execute(update_second_place)
                if name == sorted_storage[2]:
                    third_place = db_data[0][7] + 1
                    update_third_place = f"UPDATE statistic SET third_places = {third_place} WHERE player_id = " \
                                 f"(SELECT player_id  FROM statistic JOIN players " \
                                     f"ON players.id = statistic.player_id " \
                                 f"WHERE players.name = '{name}')"
                    self.cursor.execute(update_third_place)
            self.connection.commit()

    def show_statistic(self):
        all_statistic = f"SELECT players.name, number_of_games,max_points_in_game, avg_points_per_game," \
                        f"first_places,second_places,third_places " \
                      f"FROM players JOIN statistic " \
                      f"ON players.id = statistic.player_id"
        list_of_statistic = self.cursor.execute(all_statistic).fetchall()
        columns = ['Имя', 'Кол-во игр', 'Макс. очков за игру',
                   'Сред. кол-во очков за игру','1-ых мест', '2-ых мест', '3-их мест']

        print(pandas.DataFrame(data=list_of_statistic, columns=columns))
