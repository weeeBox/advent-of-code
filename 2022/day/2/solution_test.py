import unittest

import sys
from typing import Tuple

sys.path.append('../../helpers')

from helpers import read_int
from solution import Round, ROCK, PAPER, SCISSORS, get_shape_score, get_round_score, solve

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

    def test_score_small_case(self):
        expected = read_int('test/output.txt')
        actual = solve('test/input.txt')
        self.assertEqual(expected, actual)

    def test_score_large_case(self):
        expected = read_int('test/output-large.txt')
        actual = solve('input.txt')
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
