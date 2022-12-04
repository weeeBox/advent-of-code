import sys
from typing import Tuple

sys.path.append('../../helpers')

from helpers import read_values
from collections import namedtuple

ROCK, PAPER, SCISSORS = 'R', 'P', 'S'
LOST, WON, DRAW = 'L', 'W', 'D'

_SHAPE_SCORES = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3,
}

_ROUND_SCORES = {
    LOST: 0,
    DRAW: 3,
    WON: 6,
}

_YOU_WIN_ROUNDS = {
    (ROCK, SCISSORS),
    (SCISSORS, PAPER),
    (PAPER, ROCK),
}

_WIN_SHAPE = {
    second: first for first, second in _YOU_WIN_ROUNDS
}

_LOOSE_SHAPE = {
    first: second for first, second in _YOU_WIN_ROUNDS
}

_CODE_LOOKUP = {
    'A': ROCK,
    'B': PAPER,
    'C': SCISSORS,
    'X': ROCK,
    'Y': PAPER,
    'Z': SCISSORS
}


def get_win_shape(shape: str) -> str:
    return _WIN_SHAPE[shape]


def get_loose_shape(shape: str) -> str:
    return _LOOSE_SHAPE[shape]


def get_draw_shape(shape: str) -> str:
    return shape


_STRATEGY_LOOKUP = {
    'X': get_loose_shape,
    'Y': get_draw_shape,
    'Z': get_win_shape,
}

Round = namedtuple('Round', ('you', 'opponent'))


def get_shape_score(shape: str) -> int:
    return _SHAPE_SCORES[shape]


def get_round_outcome(round: Round) -> str:
    if is_draw_round(round):
        return DRAW

    return WON if round in _YOU_WIN_ROUNDS else LOST


def is_draw_round(round: Round) -> bool:
    return round.you == round.opponent


def get_round_score(round: Round) -> int:
    outcome = get_round_outcome(round)
    return _ROUND_SCORES[outcome]


def get_score(rounds: Tuple[Round, ...]) -> int:
    total = 0
    for round in rounds:
        total += get_shape_score(round.you) + get_round_score(round)

    return total


def parse_round_part1(value: str) -> Round:
    opponent, you = value.split(' ')
    # we flip the values to make code more intuitive
    return Round(you=_CODE_LOOKUP[you], opponent=_CODE_LOOKUP[opponent])


def parse_round_part2(value: str) -> Round:
    opponent_code, strategy_code = value.split(' ')
    opponent = _CODE_LOOKUP[opponent_code]
    get_shape = _STRATEGY_LOOKUP[strategy_code]
    you = get_shape(opponent)

    # we flip the values to make code more intuitive
    return Round(you, opponent)


def _solve(path, parser):
    rounds = read_values(path, parser=parser)
    return get_score(rounds)


def solve_part1(path) -> int:
    return _solve(path, parser=parse_round_part1)


def solve_part2(path) -> int:
    return _solve(path, parser=parse_round_part2)
