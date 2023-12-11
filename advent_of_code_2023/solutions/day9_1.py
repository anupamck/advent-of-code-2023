import re
import os
from functools import reduce


def find_next_value(values):
    next_value = values[-1]
    while list(set(values)) != [0]:
        values = list(map(lambda x, y: y - x, values[: -1], values[1:]))
        next_value += values[-1]
    return next_value


if __name__ == '__main__':
    input_file_path = os.path.join("advent_of_code_2023", "inputs", "day9.txt")
    with open(input_file_path) as input_file:
        env_values = []
        for line in input_file:
            sequence = line.split(' ')
            sequence = list(map(lambda value: int(value.strip()), sequence))
            env_values.append(sequence)
        sum_of_next_values = 0
        for value_set in env_values:
            sum_of_next_values += find_next_value(value_set)
        print(sum_of_next_values)
