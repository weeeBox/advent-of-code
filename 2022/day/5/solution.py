import sys
from pprint import pprint
from typing import Tuple

sys.path.append('../../helpers')

from helpers import read_values, parse_values
from range import Range, parse_range
from collections import defaultdict, namedtuple

Operation = namedtuple('Operation', ('src', 'dst', 'count'))

_EMPTY = ' '


def _parse_tokens(line: str) -> tuple:
    i = 0
    tokens = []
    while i < len(line):
        i += 1  # '['
        tokens.append(line[i] if line[i] != _EMPTY else None)  # X
        i += 3  # '] '

    return tuple(tokens)


def _read_crates_and_ops(path: str) -> Tuple[dict, tuple]:
    lines = read_values(path)

    line_idx = 0
    # parsing tokens
    all_tokens = []
    while line_idx < len(lines):
        line = lines[line_idx]
        if len(line) == 0:
            break

        all_tokens.append(_parse_tokens(line))
        line_idx += 1

    lookup = dict()
    numbers = all_tokens[-1]

    # iterate over each stack
    for j in range(len(numbers)):
        stack = []
        # iterate over rows in a reverse order
        for i in reversed(range(len(all_tokens) - 1)):
            token = all_tokens[i][j]
            if token is None:
                break

            stack.append(token)

        lookup[numbers[j]] = stack

    # skipping empty line
    line_idx += 1

    # read ops
    ops = []
    import re
    pattern = re.compile(r'move (\d+) from (\d+) to (\d+)')
    while line_idx < len(lines):
        res = pattern.match(lines[line_idx])
        count, src, dst = int(res[1]), res[2], res[3]
        ops.append(Operation(src, dst, count))
        line_idx += 1

    return dict(lookup), tuple(ops)


def _simulate(stacks: dict, ops: Tuple[Operation]) -> dict:
    res = {number: list(crates) for number, crates in stacks.items()}
    for src, dst, count in ops:
        while count > 0:
            res[dst].append(res[src].pop())
            count -= 1
    return res


def get_top_crates(path: str) -> str:
    crates, ops = _read_crates_and_ops(path)
    new_crates = _simulate(crates, ops)

    return ''.join(new_crates[number][-1] for number in sorted(new_crates.keys()))
