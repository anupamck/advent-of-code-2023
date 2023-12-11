import math
import re
import os


string_rank_list = ['T', 'J', 'Q', 'K', 'A']


def which_of_a_kind(hand):
    highest_frequency = 1
    for card in hand:
        frequency = hand.count(card)
        if frequency > highest_frequency:
            highest_frequency = frequency
    return highest_frequency


def return_higher_card(card1, card2):
    if not card1.isdigit() and card2.isdigit():
        return card1
    if card1.isdigit() and not card2.isdigit():
        return card2
    if card1.isdigit() and card2.isdigit():
        if int(card1) > int(card2):
            return card1
        return card2
    if string_rank_list.index(card1) > string_rank_list.index(card2):
        return card1
    return card2


def is_treble_full_house(hand):
    for card in hand:
        frequency = hand.count(card)
        if frequency == 2:
            return True
    return False


def is_same_kind_hand_higher(hand1, hand2):
    which_kind = which_of_a_kind(hand1)
    if which_kind == 3:
        if is_treble_full_house(hand1) and not is_treble_full_house(hand2):
            return True
        if is_treble_full_house(hand2) and not is_treble_full_house(hand1):
            return False
    if which_kind == 2:
        if is_double_pair(hand1) and not is_double_pair(hand2):
            return True
        if is_double_pair(hand2) and not is_double_pair(hand1):
            return False
    return is_higher_second_order(hand1, hand2)


def is_double_pair(hand):
    number_of_pairs = 0
    for card in set(hand):
        frequency = hand.count(card)
        if frequency == 2:
            number_of_pairs += 1
    if number_of_pairs == 2:
        return True
    return False


def is_higher_second_order(hand1, hand2):
    for index, card in enumerate(hand1):
        card2 = hand2[index]
        if card == card2:
            continue
        if card == return_higher_card(card, card2):
            return True
        return False


def is_hand_higher(hand1, hand2):
    if which_of_a_kind(hand1) > which_of_a_kind(hand2):
        return True
    if which_of_a_kind(hand2) > which_of_a_kind(hand1):
        return False
    return is_same_kind_hand_higher(hand1, hand2)


def sort(pile_of_hands):
    if len(pile_of_hands) > 1:
        pile_of_hands1 = pile_of_hands[0: math.ceil(len(pile_of_hands) / 2)]
        pile_of_hands2 = pile_of_hands[len(pile_of_hands1):]
        sorted_pile_of_hands1 = sort(pile_of_hands1)
        sorted_pile_of_hands2 = sort(pile_of_hands2)
        return merge(sorted_pile_of_hands1, sorted_pile_of_hands2)
    else:
        return (pile_of_hands)


def merge(pile_of_hands1, pile_of_hands2):
    sorted_pile = []
    while len(pile_of_hands1) > 0 and len(pile_of_hands2) > 0:
        if is_hand_higher(pile_of_hands1[0], pile_of_hands2[0]):
            sorted_pile.append(pile_of_hands1.pop(0))
        else:
            sorted_pile.append(pile_of_hands2.pop(0))
    if len(pile_of_hands1) > 0:
        sorted_pile += pile_of_hands1
    else:
        sorted_pile += pile_of_hands2
    return sorted_pile


def get_games(raw_games):
    games = {}
    for raw_game in raw_games:
        hand = re.search(r'[0-9a-zA-Z_]+(?=\s\d)', raw_game).group(0)
        bid = re.search(r'(?<=\s)\d+', raw_game).group(0)
        games[hand] = int(bid)
    return games


if __name__ == '__main__':
    input_file_path = os.path.join("advent_of_code_2023", "inputs", "13.txt")
    with open(input_file_path) as input_file:
        raw_games = input_file.readlines()
        games = get_games(raw_games)
        pile_of_hands = sort(list(games.keys()))
        print(pile_of_hands)
        total_winnings = 0
        for index, hand in enumerate(pile_of_hands):
            rank = len(pile_of_hands) - index
            bid = games[hand]
            total_winnings += rank * bid
        print(total_winnings)
