from __future__ import annotations

import numpy as np
from numba import njit
from numba.typed import List

LINE_SIZE = 7  # count, color, 5 potential colors


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
def arrange_tiles(res, pattern, colors, m=0):
    line = pattern[m, :]
    compatible_colors = line[2:] & colors

    if line[1] != -1:
        forced_mask = np.zeros(5, dtype=np.int8)
        forced_mask[line[1]] = compatible_colors[line[1]]
        compatible_colors = forced_mask

    if not compatible_colors.any():
        if m == 4:
            res.append(copy_pattern(pattern))
        else:
            arrange_tiles(res, pattern, colors, m + 1)
        return

    while compatible_colors.any():
        pattern_copy = copy_pattern(pattern)
        line_copy = copy_line(line)

        chosen_color = int(np.argmax(compatible_colors))
        compatible_colors[chosen_color] = 0

        line_copy[1] = chosen_color
        line_copy[0] += 2
        pattern_copy[m, :] = line_copy

        if m == 4:
            res.append(pattern_copy)
        else:
            colors_copy = colors.copy()
            colors_copy[chosen_color] = 0
            arrange_tiles(res, pattern_copy, np.roll(colors_copy, 1), m + 1)


@njit
def all_placements(input_pattern):
    res = List()
    for _ in range(0):  # placeholder to set type
        res.append(np.zeros((5, LINE_SIZE), dtype=np.int8))
    arrange_tiles(res, input_pattern, np.ones(5, dtype=np.int8), 0)
    return res
