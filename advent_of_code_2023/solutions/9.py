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


if __name__ == '__main__':
    input_file_path = os.path.join("advent_of_code_2023", "inputs", "9.txt")
    with open(input_file_path) as input_file:
        seeds = get_seeds(input_file.readline(0))
        input_file.seek(0)
        print(seeds, "are seeds")
        seed_to_soil_map = get_map('seed-to-soil', input_file.read())
        input_file.seek(0)
        soils = transform(seeds, seed_to_soil_map)
        print(soils, "are soils")
        soil_to_fertilizer_map = get_map(
            'soil-to-fertilizer', input_file.read())
        input_file.seek(0)
        fertilizers = transform(soils, soil_to_fertilizer_map)
        print(fertilizers, "are fertilizers")
        fertilizer_to_water_map = get_map(
            'fertilizer-to-water', input_file.read())
        input_file.seek(0)
        water = transform(fertilizers, fertilizer_to_water_map)
        print(water, "is water")
        water_to_light_map = get_map(
            'water-to-light', input_file.read())
        input_file.seek(0)
        light = transform(water, water_to_light_map)
        print(light, "is light")
        light_to_temperature_map = get_map(
            'light-to-temperature', input_file.read())
        input_file.seek(0)
        temperature = transform(light, light_to_temperature_map)
        print(temperature, "is temperature")
        temperature_to_humidity_map = get_map(
            'temperature-to-humidity', input_file.read())
        input_file.seek(0)
        humidity = transform(temperature, temperature_to_humidity_map)
        print(humidity, "is humidity")
        humidity_to_location_map = get_map(
            'humidity-to-location', input_file.read())
        input_file.seek(0)
        location = transform(humidity, humidity_to_location_map)
        print(location, "is location")
        print(min(location), "is the nearest location")
