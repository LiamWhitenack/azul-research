import numpy as np
from numba import njit
from numba.typed import List

from azul.score import score_placement

LINE_SIZE = 7  # count, color, potential_colors0..4


@njit
def resolve_placement(
    score: int, path: List, wall: np.ndarray
) -> tuple[int, List, np.ndarray]:
    """
    Apply placement rules to the last pattern in path:
    - Update score if count > row index
    - Reset line state after placement
    """
    last_pattern = path[-1]

    for m in range(last_pattern.shape[0]):
        line = last_pattern[m, :]
        if line[0] > m:  # count > row index
            # Score placement
            score += score_placement(wall, m, line[1])
            wall[m, line[1]] = 1
            # Reset line
            line[2 + line[1]] = 0  # potential_colors
            line[1] = -1  # color
            line[0] = 0  # count

    # Optional end-of-turn logic
    if np.sum(wall) < 2:
        pass  # placeholder

    return score, path, wall
