import os

number_map = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'zero': 0,
}


def get_first_number(line, number_map):
    letters = ''
    for i in range(len(line)):
        if line[i].isdigit():
            return line[i]
        letters = letters + (line[i])
        for number_text, number in number_map.items():
            if number_text in letters:
                return str(number)


def get_last_number(line, number_map):
    line = line[::-1]
    letters = ''
    for i in range(len(line)):
        if line[i].isdigit():
            return line[i]
        letters = (line[i]) + letters
        for number_text, number in number_map.items():
            if number_text in letters:
                return str(number)


def get_calibration_values(input_text):
    return [int(get_first_number(line, number_map) + get_last_number(line, number_map)) for line in input_text]


if __name__ == '__main__':
    input_file_path = os.path.join("advent_of_code_2023", 'inputs', '1.txt')
    with open(input_file_path, 'r') as input_file:
        input_text = input_file.readlines()
        calibration_values = get_calibration_values(input_text)
        print(sum(calibration_values))
