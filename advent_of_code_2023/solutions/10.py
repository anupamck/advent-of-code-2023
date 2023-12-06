import os
import re


def get_nearest_location(line, input):
    seeds_string = re.search(
        '(?<=seeds:)[\d ]+', line).group(0).strip()
    seed_schema = [int(value) for value in seeds_string.split()]
    nearest_location = 9999999999
    for index, value in enumerate(seed_schema):
        if index % 2 == 0:
            for seed in range(value, value + seed_schema[index + 1]):
                location = transform_multiple(seed, map_array, input)
                if location < nearest_location:
                    nearest_location = location
                    nearest_seed = seed
    print(nearest_seed, 'nearest_seed')
    return nearest_location


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


def transform(value, map):
    transformed = False
    for row in map:
        if row[0] <= value <= row[1]:
            result = row[2] + value - row[0]
            transformed = True
            break
    if not transformed:
        return value
    else:
        return result


def transform_multiple(value, map_array, input):
    for mapping in map_array:
        map = get_map(mapping, input)
        result = transform(value, map)
        value = result
    return result


if __name__ == '__main__':
    input_file_path = os.path.join("advent_of_code_2023", "inputs", "9.txt")
    with open(input_file_path) as input_file:
        input = input_file.read()
        input_file.seek(0)
        line = input_file.readline()
        map_array = ['seed-to-soil', 'soil-to-fertilizer',
                     'fertilizer-to-water', 'water-to-light', 'light-to-temperature',
                     'temperature-to-humidity', 'humidity-to-location']
        nearest_location = get_nearest_location(line, input)
        print(nearest_location, "is the nearest location")
