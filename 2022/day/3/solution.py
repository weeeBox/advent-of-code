import sys
from typing import Tuple

sys.path.append('../../helpers')

from helpers import read_values
from collections import Counter, namedtuple

Rucksack = namedtuple('Rucksack', ('first', 'second'))

_LOWER_CASE_FIRST_PRIORITY = 1
_UPPER_CASE_FIRST_PRIORITY = 27


def _get_priority(item: str) -> int:
    first_item, first_priority = ('a', _LOWER_CASE_FIRST_PRIORITY) \
        if item.islower() \
        else ('A', _UPPER_CASE_FIRST_PRIORITY)
    return ord(item) - ord(first_item) + first_priority


def _get_rucksack_sum(rucksack):
    first, second = rucksack
    first_lookup = set(first)
    for item in second:
        if item in first_lookup:
            return _get_priority(item)

    return 0


def _get_sum_of_priorities(rucksacks):
    total = 0
    for rucksack in rucksacks:
        total += _get_rucksack_sum(rucksack)
    return total


def _parse_rucksack(value: str) -> Rucksack:
    half_size = len(value) // 2
    return Rucksack(first=value[:half_size], second=value[half_size:])


def get_sum_of_priorities(path: str) -> int:
    rucksacks = read_values(path, _parse_rucksack)
    return _get_sum_of_priorities(rucksacks)
