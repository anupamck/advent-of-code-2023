from functools import reduce


def increment_speed_till_record(initial_speed, total_time, record, increment):
    for speed in range(initial_speed, total_time + 1, increment):
        distance = (speed) * (total_time - speed)
        if distance > record:
            if increment == 1:
                return speed
            else:
                return decrement_speed_till_record(speed, total_time, record, int(increment / 10))


def decrement_speed_till_record(initial_speed, total_time, record, decrement):
    for speed in range(initial_speed, 0, - 1 * decrement):
        distance = (speed) * (total_time - speed)
        if distance < record:
            if decrement == 1:
                return speed + 1  # 1 is added back here so that a winning speed is returned
            else:
                return increment_speed_till_record(speed, total_time, record, int(decrement / 10))


if __name__ == '__main__':
    total_time = 44806572
    record = 208158110501102

    lowest_winning_speed = increment_speed_till_record(
        0, total_time, record, 10000)
    win_possibilities = total_time - 2 * lowest_winning_speed + 1
    print(win_possibilities)
