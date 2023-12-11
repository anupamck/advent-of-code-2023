from advent_of_code_2023.solutions.day8_2 import *


def test_find_lcm_two_numbers():
    assert find_lcm_two_numbers(5, 13) == 65
    assert find_lcm_two_numbers(1, 8) == 8


def test_find_lcm():
    assert find_lcm([8, 7, 24]) == 168
    assert find_lcm([56]) == 56


def test_find_gcd():
    assert find_gcd(252, 105) == 21
