from functools import reduce


def product_of_win_possibilities(win_possibilities):
    return reduce(lambda x, y: x * y, win_possibilities)


if __name__ == '__main__':
    time_and_records = {
        44806572: 208158110501102
    }

    time_and_records_test = {
        7: 9,
        15: 40,
        30: 200
    }

    win_possibilities = []

    for time, record in time_and_records.items():
        for i in range(time + 1):
            distance = (i) * (time - i)
            if distance > record:
                win_possibilities.append(time - 2 * i + 1)
                break

    print(win_possibilities, "win_possibilities")
    # print(product_of_win_possibilities(win_possibilities), "margin_of_error")
