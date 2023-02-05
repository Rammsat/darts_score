import os.path
import sqlite3
from sqlite3 import Error


def create_connection():
    path_db = os.path.abspath('darts.db')
    connection = None
    try:
        connection = sqlite3.connect(path_db)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        result = cursor.execute(query).fetchall()
        connection.commit()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


connection = create_connection()
name = "Гриша"
update_script = f"UPDATE players SET games = 5 WHERE names = '{name}'"
#update = execute_read_query(connection, update_script)

select_script = f"SELECT number_of_games, max_points_in_game, avg_points_per_game FROM statistic JOIN players ON" \
                 f" players.id = statistic.player_id " \
                 f"where name = '{name}'"
select = execute_read_query(connection, select_script)
pars = select[0][0]
print(select)

