import re
import os


def count_steps_to_destination(map, directions):
    current_location = 'AAA'
    steps = 0
    while current_location != 'ZZZ':
        for direction in directions:
            steps += 1
            if direction == 'L':
                current_location = map[current_location][0]
            else:
                current_location = map[current_location][1]
            if current_location == 'ZZZ':
                break
    return steps


if __name__ == '__main__':
    input_file_path = os.path.join("advent_of_code_2023", "inputs", "15.txt")
    with open(input_file_path) as input_file:
        directions_string = input_file.readline().strip()
        directions = list(directions_string)
        map = {}
        key_pattern = r'[a-z, A-Z]+(?= \=)'
        value_pattern = r'(?<=\= \()[a-z, A-Z]+'
        for line in input_file:
            if re.search(key_pattern, line):
                key = re.search(key_pattern, line).group(0)
                value = re.search(value_pattern, line).group(0).split(', ')
                map[key] = value
        print(count_steps_to_destination(map, directions))
