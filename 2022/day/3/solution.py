import sys
from typing import Tuple

sys.path.append('../../helpers')

from helpers import read_values
from collections import defaultdict, namedtuple

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


def _get_sum_of_priorities(rucksacks) -> int:
    total = 0
    for rucksack in rucksacks:
        total += _get_rucksack_sum(rucksack)
    return total


def _get_group_token(group):
    counts = defaultdict(int)

    def get_unique(rucksack: Rucksack) -> set:
        return set(rucksack.first + rucksack.second)

    for unique in map(get_unique, group):
        for item in unique:
            counts[item] += 1

    for item, count in counts.items():
        if count == len(group):
            return item

    raise ValueError('Token not found')


def _get_sum_of_token_priorities(groups) -> int:
    total = 0
    for group in groups:
        token = _get_group_token(group)
        total += _get_priority(token)
    return total


def _parse_rucksack(value: str) -> Rucksack:
    half_size = len(value) // 2
    return Rucksack(first=value[:half_size], second=value[half_size:])


def get_sum_of_priorities(path: str) -> int:
    rucksacks = read_values(path, _parse_rucksack)
    return _get_sum_of_priorities(rucksacks)


def _group_rucksacks(rucksacks, group_size) -> tuple:
    res = []
    for group_index in range(len(rucksacks) // group_size):
        res.append(rucksacks[group_index * group_size: (group_index + 1) * group_size])

    return tuple(res)


def get_sum_of_token_priorities(path: str) -> int:
    rucksacks = read_values(path, _parse_rucksack)
    groups = _group_rucksacks(rucksacks, group_size=3)
    return _get_sum_of_token_priorities(groups)
