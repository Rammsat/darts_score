import os.path
import sqlite3
from sqlite3 import Error


def create_connection_to_db():
    path_db = os.path.abspath('darts.db')
    connection = None
    try:
        connection = sqlite3.connect(path_db)
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


def update_statistics(connection, storage: dict):
    cursor = connection.cursor()

    for name in storage:
        select_data = f"SELECT number_of_games, max_points_in_game, avg_points_per_game " \
                      f"FROM statistic JOIN players ON" \
                      f" players.id = statistic.player_id " f"where name = '{name}'"
        db_data = cursor.execute(select_data).fetchall()

        games_number = db_data[0][0] + 1
        update_games = f"UPDATE statistic SET number_of_games = {games_number} WHERE player_id = " \
                       f"(SELECT player_id  FROM statistic JOIN players ON players.id = statistic.player_id " \
                       f"WHERE players.name = '{name}')"
        cursor.execute(update_games)

        avg_points = (db_data[0][2] + storage[name]) / games_number
        update_avg_points = f"UPDATE statistic SET avg_points_per_game = {avg_points} WHERE player_id = " \
                            f"(SELECT player_id  FROM statistic JOIN players ON players.id = statistic.player_id " \
                            f"WHERE players.name = '{name}')"
        cursor.execute(update_avg_points)

        if db_data[0][1] < storage[name]:
            update_max_points = f"UPDATE statistic SET max_points_in_game = {storage[name]} WHERE player_id = " \
                                f"(SELECT player_id  FROM statistic JOIN players ON players.id = statistic.player_id " \
                                f"WHERE players.name = '{name}')"
            cursor.execute(update_max_points)
        connection.commit()
