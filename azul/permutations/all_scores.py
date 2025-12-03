from __future__ import annotations

import numpy as np
from numba import njit
from numba.typed import List

from azul.permutations.resolve_placement import resolve_placement

LINE_SIZE = 7  # count, color, 5 potential colors


@njit
def score_endgame(wall):
    return np.sum(wall)


@njit
def make_line():
    line = np.zeros(LINE_SIZE, dtype=np.int8)
    line[0] = 0  # count
    line[1] = -1  # color
    line[2:] = 1  # potential colors
    return line


@njit
def copy_line(line):
    return line.copy()


@njit
def copy_pattern(pattern):
    new_pattern = np.zeros_like(pattern)
    for i in range(pattern.shape[0]):
        new_pattern[i, :] = copy_line(pattern[i, :])
    return new_pattern


@njit
def all_placements(pattern):
    # placeholder: just return a list with the same pattern
    res = List()
    res.append(copy_pattern(pattern))
    return res


@njit
def get_all_scores(starting_score=0, n_rounds=5):
    res = List()
    unfinished = List()

    # Initialize path
    initial_pattern = np.zeros((5, LINE_SIZE), dtype=np.int8)
    for i in range(5):
        initial_pattern[i, 0] = 0
        initial_pattern[i, 1] = -1
        initial_pattern[i, 2:] = 1

    initial_path = List()
    initial_path.append(initial_pattern)

    initial_wall = np.zeros((5, 5), dtype=np.int8)
    unfinished.append((starting_score, initial_path, initial_wall))

    while len(unfinished) > 0:
        score, path, wall = unfinished.pop(0)

        if len(path) == n_rounds + 1:
            score += score_endgame(wall)
            res.append((score, path, wall))
            continue

        last_pattern = path[-1]
        placements = all_placements(last_pattern)

        for pattern_lines in placements:
            new_path = List()
            for p in path:
                new_path.append(p)
            new_path.append(pattern_lines)

            new_wall = wall.copy()

            # Apply resolve_placement
            updated_score, updated_path, updated_wall = resolve_placement(
                score, new_path, new_wall
            )
            unfinished.append((updated_score, updated_path, updated_wall))

    return res
