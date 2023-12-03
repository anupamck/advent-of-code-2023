import re
import os


def get_number_of_cubes(colour, game):
    pattern = "\d+(?= " + colour + ")"
    matches = re.search(pattern, game)
    if matches:
        return int(matches.group(0))
    return 0


def is_game_possible(game):
    red_cubes = get_number_of_cubes('red', game)
    green_cubes = get_number_of_cubes('green', game)
    blue_cubes = get_number_of_cubes('blue', game)
    if red_cubes > red_cube_limit or blue_cubes > blue_cube_limit or green_cubes > green_cube_limit:
        return False
    return True


if __name__ == '__main__':
    input_file_path = os.path.join("advent_of_code_2023", 'inputs', '3.txt')
    red_cube_limit = 12
    green_cube_limit = 13
    blue_cube_limit = 14
    possible_games = []
    with open(input_file_path) as input_file:
        input_text = input_file.readlines()
        for line in input_text:
            game_number = int(line.split(":", 1)[0].replace("Game ", ""))
            game_details = line.split(":", 1)[1]
            games = game_details.split(";")
            has_impossible_game = False
            for game in games:
                if not is_game_possible(game):
                    has_impossible_game = True
            if not has_impossible_game:
                possible_games.append(game_number)
    print(possible_games)
    print(sum(possible_games))
