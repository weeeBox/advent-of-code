import unittest

from range import Range, parse_range


class MyTestCase(unittest.TestCase):
    def test_parse_range(self):
        self.assertEqual(Range(2, 6), parse_range('2-6'))

    def test_overlaps(self):
        self.assertTrue(Range(1, 6).overlaps(Range(2, 8)))
        self.assertTrue(Range(2, 8).overlaps(Range(1, 6)))

        self.assertTrue(Range(1, 6).overlaps(Range(6, 8)))
        self.assertTrue(Range(6, 8).overlaps(Range(1, 6)))

        self.assertFalse(Range(1, 6).overlaps(Range(7, 8)))
        self.assertFalse(Range(7, 8).overlaps(Range(1, 6)))

    def test_fully_overlaps(self):
        self.assertTrue(Range(1, 6).fully_overlaps(Range(2, 4)))
        self.assertTrue(Range(2, 4).fully_overlaps(Range(1, 6)))

        self.assertTrue(Range(1, 6).fully_overlaps(Range(1, 4)))
        self.assertTrue(Range(1, 4).fully_overlaps(Range(1, 6)))

        self.assertTrue(Range(1, 6).fully_overlaps(Range(2, 6)))
        self.assertTrue(Range(2, 6).fully_overlaps(Range(1, 6)))

        self.assertFalse(Range(1, 6).fully_overlaps(Range(2, 7)))
        self.assertFalse(Range(2, 7).fully_overlaps(Range(1, 6)))

        self.assertFalse(Range(1, 6).fully_overlaps(Range(6, 8)))
        self.assertFalse(Range(6, 8).fully_overlaps(Range(1, 6)))

        self.assertFalse(Range(1, 6).fully_overlaps(Range(7, 8)))
        self.assertFalse(Range(7, 8).fully_overlaps(Range(1, 6)))


if __name__ == '__main__':
    unittest.main()
