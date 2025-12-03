import numpy as np
from numba import njit


@njit(cache=True)
def score_placement(wall: np.ndarray, m: int, n: int) -> int:
    if wall[m, n]:
        raise Exception("A piece has already been placed in that position!")

    score_row, score_column = False, False
    points = 1

    # Check row to the right
    for ni in range(n + 1, 5):
        if not wall[m, ni]:
            break
        score_row = True
        points += 1

    # Check row to the left
    for ni in range(1, n + 1):
        if not wall[m, n - ni]:
            break
        score_row = True
        points += 1

    # Check column downwards
    for mi in range(m + 1, 5):
        if not wall[mi, n]:
            break
        score_column = True
        points += 1

    # Check column upwards
    for mi in range(1, m + 1):
        if not wall[m - mi, n]:
            break
        score_column = True
        points += 1

    if score_row and score_column:
        points += 1

    return points


@njit(cache=True)
def score_endgame(wall: np.ndarray) -> int:
    res = 0

    # Full rows
    for m in range(5):
        full_row = True
        for n in range(5):
            if not wall[m, n]:
                full_row = False
                break
        if full_row:
            res += 2

    # Full columns
    for n in range(5):
        full_col = True
        for m in range(5):
            if not wall[m, n]:
                full_col = False
                break
        if full_col:
            res += 7

    # Full diagonals (top-left to bottom-right pattern)
    for n in range(5):
        full_diag = True
        for i in range(5):
            if not wall[i % 5, (n + i) % 5]:
                full_diag = False
                break
        if full_diag:
            res += 10

    return res
