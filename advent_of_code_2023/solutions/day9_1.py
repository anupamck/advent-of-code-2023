import os


def find_next_value(values):
    def find_next_value_cumulative(values, last_value):
        if list(set(values)) == [0]:
            return last_value
        else:
            new_value = list(map(lambda a, b: b - a, values[:-1], values[1:]))
            return find_next_value_cumulative(new_value, last_value + new_value[-1])
    return find_next_value_cumulative(values, values[-1])


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
