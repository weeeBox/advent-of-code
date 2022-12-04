import unittest

import sys
from typing import Tuple

sys.path.append('../../helpers')

from helpers import read_int
from solution import Round, ROCK, PAPER, SCISSORS, get_shape_score, get_round_score, solve_part1, solve_part2

WON_SCORE, DRAW_SCORE, LOST_SCORE, = 6, 3, 0


class MyTestCase(unittest.TestCase):
    def test_shape_score(self):
        self.assertEqual(1, get_shape_score(ROCK))
        self.assertEqual(2, get_shape_score(PAPER))
        self.assertEqual(3, get_shape_score(SCISSORS))

    def test_round_scores(self):
        self.assertEqual(WON_SCORE, get_round_score(Round(ROCK, SCISSORS)))
        self.assertEqual(LOST_SCORE, get_round_score(Round(ROCK, PAPER)))
        self.assertEqual(DRAW_SCORE, get_round_score(Round(ROCK, ROCK)))

        self.assertEqual(LOST_SCORE, get_round_score(Round(SCISSORS, ROCK)))
        self.assertEqual(WON_SCORE, get_round_score(Round(SCISSORS, PAPER)))
        self.assertEqual(DRAW_SCORE, get_round_score(Round(SCISSORS, SCISSORS)))

        self.assertEqual(WON_SCORE, get_round_score(Round(PAPER, ROCK)))
        self.assertEqual(LOST_SCORE, get_round_score(Round(PAPER, SCISSORS)))
        self.assertEqual(DRAW_SCORE, get_round_score(Round(PAPER, PAPER)))

    def test_score_small_input_part_1(self):
        expected = read_int('test/output-small-part1.txt')
        actual = solve_part1('test/input-small.txt')
        self.assertEqual(expected, actual)

    def test_score_large_input_part_1(self):
        expected = read_int('test/output-large-part1.txt')
        actual = solve_part1('test/input-large.txt')
        self.assertEqual(expected, actual)

    def test_score_small_input_part_2(self):
        expected = read_int('test/output-small-part2.txt')
        actual = solve_part2('test/input-small.txt')
        self.assertEqual(expected, actual)

    def test_score_large_input_part_2(self):
        expected = read_int('test/output-large-part2.txt')
        actual = solve_part2('test/input-large.txt')
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
