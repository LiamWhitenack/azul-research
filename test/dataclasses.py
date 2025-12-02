from dataclasses import dataclass

import numpy as np


@dataclass
class ScorePlacementTestCase:
    id: str
    wall: np.ndarray
    m: int
    n: int
    expected: int


@dataclass
class ScoreEndgameTestCase:
    id: str
    wall: np.ndarray
    expected: int
