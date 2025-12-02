from typing import Annotated

import numpy as np
from numpy.typing import NDArray

WallType = Annotated[NDArray[np.bool_], (5, 5)]


def score(wall: WallType, m: int, n: int) -> int:
    if wall[m, n]:
        raise Exception("A piece has already been placed in that position!")
    score_row, score_column = False, False
    points = 1
    for ni in range(n + 1, 5):
        if not wall[m, ni]:
            break
        score_row = True
        points += 1
    for ni in range(1, n + 1):
        if not wall[m, n - ni]:
            break
        score_row = True
        points += 1
    for mi in range(m + 1, 5):
        if not wall[mi, n]:
            break
        score_column = True
        points += 1
    for mi in range(1, m + 1):
        if not wall[m - mi, n]:
            break
        score_column = True
        points += 1

    if score_row and score_column:
        points += 1

    return points
