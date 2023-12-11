import os


def find_previous_value(values):
    if list(set(values)) == [0]:
        return 0
    else:
        new_values = list(map(lambda a, b: b - a, values[:-1], values[1:]))
        return (values[0] - find_previous_value(new_values))


if __name__ == '__main__':
    input_file_path = os.path.join("advent_of_code_2023", "inputs", "day9.txt")
    with open(input_file_path) as input_file:
        env_values = []
        for line in input_file:
            sequence = line.split(' ')
            sequence = list(map(lambda value: int(value.strip()), sequence))
            env_values.append(sequence)
        sum_of_previous_values = 0
        for value_set in env_values:
            sum_of_previous_values += find_previous_value(value_set)
        print(sum_of_previous_values)
