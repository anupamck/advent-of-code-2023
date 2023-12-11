import re
import os
from functools import reduce


def find_gear_indices(line):

    gear_indices = []

    for i in range(len(line)):

        if re.match(r'\*', line[i]):

            gear_indices.append(i)

    return gear_indices


def append_adjacent_gear_ratios(line, index, gear_ratios):

    if (index - 1) >= 0 and line[index - 1].isdigit():

        start_index = find_number_start_index(line, index - 1)

        part_number_to_left = construct_ratio_from_index(line, start_index)
        gear_ratios.append(int(part_number_to_left))

    if (index + 1) < len(line) and line[index + 1].isdigit():

        part_number_to_right = construct_ratio_from_index(line, index + 1)

        gear_ratios.append(int(part_number_to_right))

    return gear_ratios


def append_gear_ratios_from_line_above_or_below(line_above_or_below, index, gear_ratios):

    if line_above_or_below[index].isdigit():

        start_index = find_number_start_index(line_above_or_below, index)

        gear_ratio_above_or_below = construct_ratio_from_index(
            line_above_or_below, start_index)

        gear_ratios.append(int(gear_ratio_above_or_below))
        return

    if (index - 1) >= 0 and line_above_or_below[index - 1].isdigit() or (index+1) < len(line) and line_above_or_below[index + 1].isdigit():
        append_adjacent_gear_ratios(line_above_or_below, index, gear_ratios)
        return


def construct_ratio_from_index(line, start_index):

    if start_index < len(line) and line[start_index].isdigit():

        return line[start_index] + construct_ratio_from_index(line, start_index + 1)

    else:

        return ''


def find_number_start_index(line, index):

    if (index - 1) >= 0 and line[index - 1].isdigit():

        return find_number_start_index(line, index - 1)

    else:
        return int(index)


def product_of_gear_ratios(gear_ratios):
    return reduce(lambda x, y: x * y, gear_ratios)


if __name__ == '__main__':
    input_file_path = os.path.join("advent_of_code_2023", "inputs", "5.txt")
    sum_product_of_gear_ratios = 0

    with open(input_file_path) as input_file:
        lines = input_file.readlines()

        for index, line in enumerate(lines):
            gear_indices = find_gear_indices(line)

            for gear_index in gear_indices:
                gear_ratios = []
                append_adjacent_gear_ratios(line, gear_index, gear_ratios)

                if index > 0:
                    append_gear_ratios_from_line_above_or_below(
                        lines[index - 1], gear_index, gear_ratios)

                if index < len(lines) - 1:
                    append_gear_ratios_from_line_above_or_below(
                        lines[index + 1], gear_index, gear_ratios)

                if len(gear_ratios) > 1:
                    sum_product_of_gear_ratios = sum_product_of_gear_ratios + \
                        product_of_gear_ratios(gear_ratios)

    print((sum_product_of_gear_ratios),
          "is the sum-product of all gear ratios")
