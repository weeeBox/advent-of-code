import unittest

import sys
from typing import Tuple

sys.path.append('../../helpers')

from helpers import read_int, read_str
from solution import get_top_crates, get_top_crates_at_once


class MyTestCase(unittest.TestCase):
    def test_small_input_part_1(self):
        expected = read_str('test/output-small-part1.txt')
        actual = get_top_crates('test/input-small.txt')
        self.assertEqual(expected, actual)

    def test_score_large_input_part_1(self):
        expected = read_str('test/output-large-part1.txt')
        actual = get_top_crates('test/input-large.txt')
        self.assertEqual(expected, actual)

    def test_score_small_input_part_2(self):
        expected = read_str('test/output-small-part2.txt')
        actual = get_top_crates_at_once('test/input-small.txt')
        self.assertEqual(expected, actual)

    def test_score_large_input_part_2(self):
        expected = read_str('test/output-large-part2.txt')
        actual = get_top_crates_at_once('test/input-large.txt')
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
