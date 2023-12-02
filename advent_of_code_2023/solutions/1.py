import os


def get_first_number(characters):
    for i in range(len(characters)):
        # If i is a numerical value, return it
        if characters[i].isdigit():
            return characters[i]
    return None


def get_last_number(characters):
    characters = characters[::-1]
    for i in range(len(characters)):
        # If i is a numerical value, return it
        if characters[i].isdigit():
            return characters[i]
    return None


def get_calibration_values(input_text):
    calibration_values = []
    for line in input_text:
        first_number = get_first_number(line)
        last_number = get_last_number(line)
        whole_number = first_number + last_number
        calibration_values.append(int(whole_number))
    return calibration_values


if __name__ == '__main__':
    input_file_path = os.path.join("advent_of_code_2023", 'inputs', '1.txt')
    with open(input_file_path, 'r') as input_file:
        input_text = input_file.readlines()
        calibration_values = get_calibration_values(input_text)
        print(sum(calibration_values))
