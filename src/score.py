import numpy as np

from src.wall import WallType


def score_placement(wall: np.ndarray, m: int, n: int) -> int:
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


def endgame_scoring(wall: WallType) -> int:
    res = 0
    for m in range(5):
        if all(wall[m, n] for n in range(5)):
            res += 2
    for n in range(5):
        if all(wall[m, n] for m in range(5)):
            res += 7
    for n in range(5):
        if all(wall[(i) % 5, (n + i) % 5] for i in range(5)):
            res += 10
    return res
