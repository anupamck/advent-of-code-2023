import re
import os
from collections import Counter


def find_duplicates(arr):
    counts = Counter(arr)
    return [item for item, count in counts.items() if count > 1]


def find_symbol_indices(line):

    symbol_indices = []

    for i in range(len(line)):

        symbol_pattern = r'[^a-zA-Z0-9.\n]'

        if re.match(symbol_pattern, line[i]):

            symbol_indices.append(i)

    return symbol_indices


def append_adjacent_part_numbers(line, index, part_numbers):

    if (index - 1) >= 0 and line[index - 1].isdigit():

        start_index = find_number_start_index(line, index - 1)

        part_number_to_left = construct_number_from_index(line, start_index)
        part_numbers.append(int(part_number_to_left))

    if (index + 1) < len(line) and line[index + 1].isdigit():

        part_number_to_right = construct_number_from_index(line, index + 1)

        part_numbers.append(int(part_number_to_right))

    return part_numbers


def append_parts_from_line_above_or_below(line_above, index, part_numbers):

    if line_above[index].isdigit():

        start_index = find_number_start_index(line_above, index)

        part_number_above = construct_number_from_index(

            line_above, start_index)

        part_numbers.append(int(part_number_above))
        return

    if (index - 1) >= 0 and line_above[index - 1].isdigit() or (index+1) < len(line) and line_above[index + 1].isdigit():

        append_adjacent_part_numbers(line_above, index, part_numbers)
        return


def construct_number_from_index(line, start_index):

    if start_index < len(line) and line[start_index].isdigit():

        return line[start_index] + construct_number_from_index(line, start_index + 1)

    else:

        return ''


def find_number_start_index(line, index):

    if (index - 1) >= 0 and line[index - 1].isdigit():

        return find_number_start_index(line, index - 1)

    else:
        return int(index)


if __name__ == '__main__':
    input_file_path = os.path.join("advent_of_code_2023", "inputs", "5.txt")
    part_numbers = []
    with open(input_file_path) as input_file:
        lines = input_file.readlines()

        for index, line in enumerate(lines):
            symbol_indices = find_symbol_indices(line)
            for symbol_index in symbol_indices:
                append_adjacent_part_numbers(line, symbol_index, part_numbers)
                if index > 0:
                    append_parts_from_line_above_or_below(
                        lines[index - 1], symbol_index, part_numbers)

                if index < len(lines) - 1:
                    append_parts_from_line_above_or_below(
                        lines[index + 1], symbol_index, part_numbers)

    print(sum(part_numbers), "is the sum of part numbers")
