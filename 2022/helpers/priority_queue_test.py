import unittest
from priority_queue import PriorityQueue


class MyTestCase(unittest.TestCase):
    def test_min_pq(self):
        queue = PriorityQueue(ismin=True)
        queue.push(2)
        queue.push(1)
        queue.push(3)

        self.assertEqual((1, 2, 3), queue.items)

    def test_max_pq(self):
        queue = PriorityQueue(ismin=False)
        queue.push(2)
        queue.push(1)
        queue.push(3)

        self.assertEqual((3, 2, 1), queue.items)


if __name__ == '__main__':
    unittest.main()
