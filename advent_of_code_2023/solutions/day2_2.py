import re
import os


def get_max_cubes(line, colour):
    pattern = "\d+(?= " + colour + ")"
    matches = re.findall(pattern, line)
    matches_int = [int(item) for item in matches]
    return max(matches_int)
    pattern = r"(?<=Game\s)\d+"
    game_number = re.search(pattern, line).group(0)
    return int(game_number)


def find_game_power(line):
    max_blue_cubes = get_max_cubes(line, "blue")
    max_green_cubes = get_max_cubes(line, "green")
    max_red_cubes = get_max_cubes(line, "red")
    return max_blue_cubes * max_green_cubes * max_red_cubes


if __name__ == '__main__':
    input_file_path = os.path.join("advent_of_code_2023", 'inputs', '3.txt')
    game_powers = []
    with open(input_file_path) as input_file:
        games = input_file.readlines()
        for game in games:
            game_powers.append(find_game_power(game))
    print(sum(game_powers))
