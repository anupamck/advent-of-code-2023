import re
import os
from functools import reduce


def count_steps_to_destination(map, directions, start_location):
    current_location = start_location
    steps = 0
    at_destination = False
    while not current_location.endswith('Z'):
        for direction in directions:
            steps += 1
            new_location = []
            if direction == 'L':
                new_location = map[current_location][0]
            else:
                new_location = map[current_location][1]
            current_location = new_location
            if current_location.endswith('Z'):
                break
    return steps


def get_start_locations(map):
    return list(filter(lambda location: location.endswith('A'), map))


def find_lcm_two_numbers(number1, number2):
    return int(number1 * number2 / find_gcd(number1, number2))


def find_lcm(numbers):
    return reduce(lambda number1, number2: find_lcm_two_numbers(number1, number2), numbers)


def find_gcd(number1, number2):
    if number2 == 0:
        return number1
    else:
        return find_gcd(number2, number1 % number2)


if __name__ == '__main__':
    input_file_path = os.path.join("advent_of_code_2023", "inputs", "day8.txt")
    with open(input_file_path) as input_file:
        directions_string = input_file.readline().strip()
        directions = list(directions_string)
        map = {}
        key_pattern = r'[a-z, A-Z,0-9]+(?= \=)'
        value_pattern = r'(?<=\= \()[a-z, A-Z, 0-9]+'
        for line in input_file:
            if re.search(key_pattern, line):
                key = re.search(key_pattern, line).group(0)
                value = re.search(value_pattern, line).group(0).split(', ')
                map[key] = value
        start_locations = get_start_locations(map)
        list_of_steps = []
        for start_location in start_locations:
            steps = count_steps_to_destination(
                map, directions, start_location)
            list_of_steps.append(steps)
        print(find_lcm(list_of_steps))
