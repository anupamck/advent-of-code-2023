import os
import re


def find_nearest_location(seed_schema, increment):
    nearest_location = 9999999999
    for index, value in enumerate(seed_schema):
        if index % 2 == 0:
            for seed in range(value, value + seed_schema[index + 1], increment):
                location = transform_multiple(seed, map_array, input)
                if location < nearest_location:
                    nearest_location = location
                    nearest_seed = seed
    if increment == 1:
        return nearest_location
    else:
        new_seed_schema = [nearest_seed - increment, 2 * increment]
        new_increment = int(increment / 10)
        return find_nearest_location(new_seed_schema, new_increment)


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
        seeds_string = re.search(
            '(?<=seeds:)[\d ]+', line).group(0).strip()
        seed_schema = [int(value) for value in seeds_string.split()]
        map_array = ['seed-to-soil', 'soil-to-fertilizer',
                     'fertilizer-to-water', 'water-to-light', 'light-to-temperature',
                     'temperature-to-humidity', 'humidity-to-location']
        nearest_location = find_nearest_location(seed_schema, 1000000)
        print("The nearest location is", nearest_location)


#               seeds      location
# First value:  3107966111 53037249
# Second value: 3107440111 52511249
# Answer value: 3107439671 52510809
