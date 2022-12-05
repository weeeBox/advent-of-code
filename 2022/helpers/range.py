from collections import namedtuple
from helpers import parse_values

Range = namedtuple('Range', ('start', 'end'))


class Range(object):
    __slots__ = ('start', 'end')

    def __init__(self, start: int, end: int):
        if start > end:
            raise ValueError(f'Invalid range {start}-{end}')
        self.start = start
        self.end = end

    def fully_overlaps(self, other: Range) -> bool:
        return self.start <= other.start and self.end >= other.end or \
               other.start <= self.start and other.end >= self.end

    # •---•
    #  •-•

    #  •-•
    # •---•

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __str__(self):
        return f'{self.start}-{self.end}'

    def __repr__(self):
        return f'Range(start={self.start}, end={self.end})'


def parse_range(value: str) -> Range:
    tokens = parse_values(value, int, separator='-')
    if len(tokens) != 2:
        raise ValueError(f'Invalid range: {range}')

    return Range(start=int(tokens[0]), end=int(tokens[1]))
