import os.path
import sqlite3
from sqlite3 import Error


class DataBase:
    def __init__(self):
        pass

    def create_connection(self):
        path_db = os.path.abspath('../darts.db')
        self.connection = None
        try:
            self.connection = sqlite3.connect(path_db)
        except Error as e:
            print(f"The error '{e}' occurred")
        return self.connection

    def update_statistics(self, storage: dict):
        cursor = self.connection.cursor()
        sorted_storage = sorted(storage, key=storage.get, reverse=True)[:3]

        for name in sorted_storage:
            select_data = f"SELECT statistic.* " \
                          f"FROM statistic JOIN players ON" \
                          f" players.id = statistic.player_id " f"where name = '{name}'"
            db_data = cursor.execute(select_data).fetchall()
            if name == sorted_storage[0]:
                first_place = db_data[0][5] + 1
                update_first_place = f"UPDATE statistic SET first_places = {first_place} WHERE player_id = " \
                                 f"(SELECT player_id  FROM statistic JOIN players ON players.id = statistic.player_id " \
                                 f"WHERE players.name = '{name}')"
                cursor.execute(update_first_place)
            if name == sorted_storage[1]:
                second_place = db_data[0][6] + 1
                update_second_place = f"UPDATE statistic SET second_places = {second_place} WHERE player_id = " \
                                  f"(SELECT player_id  FROM statistic JOIN players ON players.id = statistic.player_id " \
                                  f"WHERE players.name = '{name}')"
                cursor.execute(update_second_place)
            if name == sorted_storage[2]:
                third_place = db_data[0][7] + 1
                update_third_place = f"UPDATE statistic SET third_places = {third_place} WHERE player_id = " \
                                 f"(SELECT player_id  FROM statistic JOIN players ON players.id = statistic.player_id " \
                                 f"WHERE players.name = '{name}')"
                cursor.execute(update_third_place)
            self.connection.commit()

        for name in storage:
            select_data = f"SELECT statistic.* " \
                      f"FROM statistic JOIN players ON" \
                      f" players.id = statistic.player_id " f"where name = '{name}'"
            db_data = cursor.execute(select_data).fetchall()

            games_number = db_data[0][1] + 1
            update_games = f"UPDATE statistic SET number_of_games = {games_number} WHERE player_id = " \
                       f"(SELECT player_id  FROM statistic JOIN players ON players.id = statistic.player_id " \
                       f"WHERE players.name = '{name}')"
            cursor.execute(update_games)

            all_points = db_data[0][4] + storage[name]
            update_all_points = f"UPDATE statistic SET all_points = {all_points} WHERE player_id = " \
                            f"(SELECT player_id  FROM statistic JOIN players ON players.id = statistic.player_id " \
                            f"WHERE players.name = '{name}')"
            cursor.execute(update_all_points)

            avg_points = all_points / games_number
            update_avg_points = f"UPDATE statistic SET avg_points_per_game = {avg_points} WHERE player_id = " \
                            f"(SELECT player_id  FROM statistic JOIN players ON players.id = statistic.player_id " \
                            f"WHERE players.name = '{name}')"
            cursor.execute(update_avg_points)

            if db_data[0][2] < storage[name]:
                update_max_points = f"UPDATE statistic SET max_points_in_game = {storage[name]} WHERE player_id = " \
                                f"(SELECT player_id  FROM statistic JOIN players ON players.id = statistic.player_id " \
                                f"WHERE players.name = '{name}')"
                cursor.execute(update_max_points)
            self.connection.commit()
