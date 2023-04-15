from app.score import Score
from app.game_preparation import GamePreparation
from app.data_base import DataBase

game_preparation = GamePreparation()
data_base = DataBase()


def main():
    while True:
        game_round = 0

        game_preparation.type_players_number()
        game_preparation.type_players_names()
        max_point = game_preparation.type_max_point()
        point_storage = game_preparation.create_player_and_points_storage()

        while True:
            game_round += 1
            score = Score(point_storage)

            points = score.type_points_of_players(game_round)
            score.show_points_and_round(game_round)

            stop_game_points = score.show_winner(max_point)
            if stop_game_points >= max_point:
                break

        data_base.create_connection()
        data_base.update_statistics(points)

if __name__ == "__main__":
    main()
