import sys
import re


def read_file():
    sum_of_successful_games = 0
    color_amounts = {"red": 12, "green": 13, "blue": 14}
    for line in sys.stdin:
        game, rounds = line.strip().split(":")
        game_number = game.split(" ")[1]
        is_valid_round = True
        for round in rounds.split(";"):
            is_valid_dice = True
            for one_color_dices in round.split(","):
                quantity, color = one_color_dices.strip().split(" ")
                if int(quantity) > color_amounts.get(color):
                    is_valid_dice = False
                    break
            if not is_valid_dice:
                is_valid_round = False
                break

        if is_valid_round:
            sum_of_successful_games += int(game_number)
    print(sum_of_successful_games)


read_file()
