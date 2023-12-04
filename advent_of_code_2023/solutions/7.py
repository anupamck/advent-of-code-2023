import re
import os


def get_winning_numbers(card):
    pattern = r'(?<=:)[\s\d]+'
    winning_numbers_string = re.search(pattern, card).group(0).strip()
    winning_numbers = re.split('\s+', winning_numbers_string)
    return winning_numbers


def get_card_numbers(card):
    pattern = r'(?<=\|)[\s\d]+'
    card_numbers_string = re.search(pattern, card).group(0).strip()
    card_numbers = re.split('\s+', card_numbers_string)
    return card_numbers


if __name__ == '__main__':
    input_file_path = os.path.join("advent_of_code_2023", "inputs", "7.txt")
    with open(input_file_path) as input_file:
        cards = input_file.readlines()
        card_total = 0
        for card in cards:
            winning_number_count = 0
            card_numbers = get_card_numbers(card)
            print(card_numbers, 'are card numbers')
            winning_numbers = get_winning_numbers(card)
            print(winning_numbers, 'are winning numbers')
            for card_number in card_numbers:
                for winning_number in winning_numbers:
                    if card_number == winning_number:
                        winning_number_count = winning_number_count + 1
                        break
            if winning_number_count > 0:
                card_total = card_total + 2**(winning_number_count-1)

    print(card_total, 'is card total')
