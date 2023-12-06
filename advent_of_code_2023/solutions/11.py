from operator import mul
from functools import reduce


def product_of_win_possibilities(win_possibilities):
    return reduce(mul, win_possibilities)


if __name__ == '__main__':
    time_and_records = {
        44: 208,
        80: 1581,
        65: 1050,
        72: 1102
    }

    win_possibilities = []

    for total_time, record in time_and_records.items():
        for speed in range(total_time + 1):
            distance = (speed) * (total_time - speed)
            if distance > record:
                win_possibilities.append(total_time - 2 * speed + 1)
                break

    print(win_possibilities, "win_possibilities")
    print(product_of_win_possibilities(win_possibilities), "margin_of_error")
