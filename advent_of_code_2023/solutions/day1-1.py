import os


def get_first_number(line):
    return next((char for char in line if char.isdigit()), None)


def get_last_number(line):
    return next((char for char in reversed(line) if char.isdigit()), None)


def get_calibration_values(input_text):
    return [int(get_first_number(line) + get_last_number(line)) for line in input_text]


if __name__ == '__main__':
    input_file_path = os.path.join("advent_of_code_2023", 'inputs', '1.txt')
    with open(input_file_path, 'r') as input_file:
        input_text = input_file.readlines()
        calibration_values = get_calibration_values(input_text)
        print(sum(calibration_values))
