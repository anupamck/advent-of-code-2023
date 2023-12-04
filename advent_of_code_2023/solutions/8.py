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
        list_of_cards = [1] * len(cards)
        for index, card in enumerate(cards):
            winning_number_count = 0
            card_numbers = get_card_numbers(card)
            winning_numbers = get_winning_numbers(card)
            for card_number in card_numbers:
                for winning_number in winning_numbers:
                    if card_number == winning_number:
                        winning_number_count = winning_number_count + 1
                        break
            if winning_number_count > 0:
                if index + winning_number_count + 1 < len(cards):
                    increment_range = index + winning_number_count + 1
                else:
                    increment_range = len(cards)
                for i in range(index + 1, increment_range):
                    list_of_cards[i] = list_of_cards[i] + \
                        list_of_cards[index]

        print(sum(list_of_cards))
