import sys
from typing import Tuple

sys.path.append('../../helpers')

from helpers import read_values, parse_values
from range import Range, parse_range
from collections import defaultdict, namedtuple


def _count_fully_overlap_ranges(pairs: tuple) -> int:
    total = 0
    for a, b in pairs:
        total += 1 if a.fully_overlaps(b) else 0

    return total


def count_fully_overlap_ranges(path: str) -> int:
    def parser(value: str) -> Tuple[Range, Range]:
        return parse_values(value, parse_range, separator=',')

    pairs = read_values(path, parser)
    return _count_fully_overlap_ranges(pairs)
