import os
import re


def get_seeds(line):
    seed_row = input_file.readlines()[0]
    seeds_string = re.search(
        '(?<=seeds:)[\d ]+', seed_row).group(0).strip()
    seeds = re.split('\s+', seeds_string)
    seeds = [int(seed) for seed in seeds]
    return seeds


def get_map(map_type, input):
    pattern = f'(?<={map_type} map:)[\n\d\s]+'
    map_rows_raw = re.search(
        pattern, input).group(0).strip().split('\n')
    map = []
    for raw_row in map_rows_raw:
        raw_row = raw_row.split(' ')
        map_row = [int(raw_row[1]), int(raw_row[1]) +
                   int(raw_row[2]) - 1, int(raw_row[0])]
        map.append(map_row)
    return map


def transform(source, map):
    result = []
    for value in source:
        transformed = False
        for row in map:
            if row[0] <= value <= row[1]:
                transformed_value = row[2] + value - row[0]
                result.append(transformed_value)
                transformed = True
                break
        if not transformed:
            result.append(value)
    return result


def transform_multiple(source, map_array, input):
    for mapping in map_array:
        map = get_map(mapping, input)
        result = transform(source, map)
        source = result
    return result


if __name__ == '__main__':
    input_file_path = os.path.join("advent_of_code_2023", "inputs", "9.txt")
    with open(input_file_path) as input_file:
        seeds = get_seeds(input_file.readline(0))
        input_file.seek(0)
        map_array = ['seed-to-soil', 'soil-to-fertilizer',
                     'fertilizer-to-water', 'water-to-light', 'light-to-temperature',
                     'temperature-to-humidity', 'humidity-to-location']

        location = transform_multiple(seeds, map_array, input_file.read())
        print(min(location), "is the nearest location")
