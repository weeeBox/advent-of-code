import sys
from typing import Tuple

sys.path.append('../../helpers')

from helpers import read_values
from priority_queue import PriorityQueue

SEPARATOR = ''


def get_max_calories(values: Tuple[str, ...], k=1) -> int:
    queue = PriorityQueue(ismin=True)

    def add_calories(value):
        queue.push(value)
        if len(queue) > k:
            queue.pop()

    curr_calories = 0
    for value in values:
        if value == SEPARATOR:
            add_calories(curr_calories)
            curr_calories = 0
        else:
            curr_calories += int(value)

    add_calories(curr_calories)

    return sum(queue.items)


if __name__ == '__main__':
    values = read_values(path='input.txt')
    print(get_max_calories(values))
    print(get_max_calories(values, k=3))
