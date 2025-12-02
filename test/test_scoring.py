from dataclasses import dataclass

import numpy as np
import pytest

from src.score import score


@dataclass
class ScoreTestCase:
    id: str
    wall: np.ndarray
    m: int
    n: int
    expected: int


TEST_CASES = [
    ScoreTestCase(
        id="Empty Wall Single Tile",
        wall=np.array(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
            dtype=bool,
        ),
        m=2,
        n=2,
        expected=1,
    ),
    ScoreTestCase(
        id="Horizontal Right Neighbor",
        wall=np.array(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
            dtype=bool,
        ),
        m=2,
        n=2,
        expected=2,
    ),
    ScoreTestCase(
        id="Horizontal Both Sides",
        wall=np.array(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 1, 0, 1, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
            dtype=bool,
        ),
        m=2,
        n=2,
        expected=3,
    ),
    ScoreTestCase(
        id="Horizontal Present But Not Adjacent 1",
        wall=np.array(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 0, 0, 1],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
            dtype=bool,
        ),
        m=2,
        n=2,
        expected=3,
    ),
    ScoreTestCase(
        id="Horizontal Present But Not Adjacent 2",
        wall=np.array(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 1, 1],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
            dtype=bool,
        ),
        m=2,
        n=2,
        expected=3,
    ),
    ScoreTestCase(
        id="Vertical Both Sides",
        wall=np.array(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
            ],
            dtype=bool,
        ),
        m=2,
        n=2,
        expected=3,
    ),
    ScoreTestCase(
        id="Cross Shape Full Bonus",
        wall=np.array(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 1, 0, 1, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
            ],
            dtype=bool,
        ),
        m=2,
        n=2,
        expected=6,
    ),
    ScoreTestCase(
        id="Edge Left Row Only",
        wall=np.array(
            [
                [0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
            ],
            dtype=bool,
        ),
        m=0,
        n=0,
        expected=2,
    ),
    ScoreTestCase(
        id="Four In Row Start",
        wall=np.array(
            [
                [0, 1, 1, 1, 1],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
            dtype=bool,
        ),
        m=0,
        n=0,
        expected=5,
    ),
    ScoreTestCase(
        id="Uneven Row And Column",
        wall=np.array(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 0, 0, 1, 0],
            ],
            dtype=bool,
        ),
        m=3,
        n=3,
        expected=5,
    ),
    ScoreTestCase(
        id="Full Wall Center",
        wall=np.array(
            [
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 0, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
            ],
            dtype=bool,
        ),
        m=2,
        n=2,
        expected=10,
    ),
]


@pytest.mark.parametrize("case", TEST_CASES, ids=[c.id for c in TEST_CASES])
def test_score(case: ScoreTestCase):
    result = score(case.wall, case.m, case.n)
    assert result == case.expected, f"{case.id}: expected {case.expected}, got {result}"
