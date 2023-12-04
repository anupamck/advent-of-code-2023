import re
import os


def get_max_cubes(line, colour):
    pattern = "\d+(?= " + colour + ")"
    matches = re.findall(pattern, line)
    matches_int = [int(item) for item in matches]
    return max(matches_int)


def get_game_number(line):
    pattern = r"(?<=Game\s)\d+"
    game_number = re.search(pattern, line).group(0)
    return int(game_number)


def is_game_possible(line):
    red_cube_limit = 12
    green_cube_limit = 13
    blue_cube_limit = 14
    max_blue_cubes = get_max_cubes(line, "blue")
    max_green_cubes = get_max_cubes(line, "green")
    max_red_cubes = get_max_cubes(line, "red")
    if max_blue_cubes > blue_cube_limit:
        return False
    max_green_cubes = get_max_cubes(line, "green")
    if max_green_cubes > green_cube_limit:
        return False
    max_red_cubes = get_max_cubes(line, "red")
    if max_red_cubes > red_cube_limit:
        return False
    return True


if __name__ == '__main__':
    input_file_path = os.path.join("advent_of_code_2023", 'inputs', '3.txt')
    possible_games = []
    with open(input_file_path) as input_file:
        input_text = input_file.readlines()
        for line in input_text:
            game_number = get_game_number(line)
            if is_game_possible(line):
                possible_games.append(int(game_number))
    print(sum(possible_games))
