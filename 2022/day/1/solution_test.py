import unittest
from solution import get_max_calories


class MyTestCase(unittest.TestCase):
    def test_top_calories_aoc_case(self):
        values = ('1000',
                  '2000',
                  '3000',
                  '',
                  '4000',
                  '',
                  '5000',
                  '6000',
                  '',
                  '7000',
                  '8000',
                  '9000',
                  '',
                  '10000')
        self.assertEqual(24000, get_max_calories(values))

    def test_top_calories_last_value(self):
        values = ('1000',
                  '2000',
                  '3000',
                  '',
                  '4000',
                  '5000',
                  '6000')
        self.assertEqual(15000, get_max_calories(values))

    def test_top_calories_single_value(self):
        values = ('1000',
                  '2000',
                  '3000')
        self.assertEqual(6000, get_max_calories(values))

    def test_top_k_calories_aoc_case(self):
        values = ('1000',
                  '2000',
                  '3000',
                  '',
                  '4000',
                  '',
                  '5000',
                  '6000',
                  '',
                  '7000',
                  '8000',
                  '9000',
                  '',
                  '10000')
        self.assertEqual(45000, get_max_calories(values, k=3))


if __name__ == '__main__':
    unittest.main()
