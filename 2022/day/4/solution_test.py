import unittest

import sys
from typing import Tuple

sys.path.append('../../helpers')

from helpers import read_int
from solution import count_fully_overlap_ranges


class MyTestCase(unittest.TestCase):
    def test_small_input_part_1(self):
        expected = read_int('test/output-small-part1.txt')
        actual = count_fully_overlap_ranges('test/input-small.txt')
        self.assertEqual(expected, actual)

    def test_score_large_input_part_1(self):
        expected = read_int('test/output-large-part1.txt')
        actual = count_fully_overlap_ranges('test/input-large.txt')
        self.assertEqual(expected, actual)

    def test_score_small_input_part_2(self):
        expected = read_int('test/output-small-part2.txt')
        actual = get_sum_of_token_priorities('test/input-small.txt')
        self.assertEqual(expected, actual)

    def test_score_large_input_part_2(self):
        expected = read_int('test/output-large-part2.txt')
        actual = get_sum_of_token_priorities('test/input-large.txt')
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
