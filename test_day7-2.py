from advent_of_code_2023.solutions.day14 import *


def test_is_higher_second_order():
    hand1 = "AAAAA"
    hand2 = "KKKKK"
    assert is_higher_second_order(hand1, hand2) == True
    hand1 = "AAKKK"
    hand2 = "AATKK"
    assert is_higher_second_order(hand1, hand2) == True
    assert is_higher_second_order("T45J5", "QQQJA") == False
    assert is_higher_second_order("JKKK2", "QQQQ2") == False


def test_which_of_a_kind():
    assert which_of_a_kind("T55J5") == 4
    assert which_of_a_kind("32T3K") == 2
    assert which_of_a_kind("JJJAT") == 4


def test_is_hand_higher():
    hand1 = ["T55J5", "QQQJA", "KKKJJ", "KKKJJ", "KK8QQ"]
    hand2 = ["32T3K", "TTTJA", "2222A", "AAA23", "AA239"]
    for i in range(len(hand1)):
        print(hand1[i], "hand1")
        print(hand2[i], "hand2")
        assert is_hand_higher(hand1[i], hand2[i]) == True


def test_return_higher_of_same_kind():
    assert is_same_kind_hand_higher("QQQJA", "TTTJA") == True


def test_is_treble_full_house():
    assert is_treble_full_house("TTJAA") == True
    assert is_treble_full_house("TTJ2A") == False


def test_is_double_pair():
    assert is_double_pair("AAKK2") == True
    assert is_double_pair("7J112") == True
    assert is_double_pair("7J142") == False
