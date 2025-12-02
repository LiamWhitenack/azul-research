import numpy as np

from src.permutations.pattern_lines import PatternLine, PatternLines


def all_placements(input: PatternLines) -> list[PatternLines]:
    placements: list[PatternLines] = []
    arrange_tiles(placements, input)
    return placements


def arrange_tiles(
    res: list[PatternLines],
    pattern: PatternLines,
    colors: np.ndarray = np.ones(5, dtype=np.bool_),  # available colors
    m: int = 0,
) -> None:
    line: PatternLine = pattern[m]

    # potential_colors is already a boolean mask now
    compatible_colors = line.potential_colors & colors

    # If a color is already chosen, restrict to only that color
    if line.color != -1:
        forced_mask = np.zeros(5, dtype=np.bool_)
        forced_mask[line.color] = compatible_colors[line.color]
        compatible_colors = forced_mask

    while compatible_colors.any():
        pattern_copy = pattern.copy()
        line_copy = line.copy()

        chosen_color = int(np.argmax(compatible_colors))
        compatible_colors[chosen_color] = False  # remove choice

        line_copy.color = chosen_color
        line_copy.count += 2
        pattern_copy[m] = line_copy

        if m == 4:
            res.append(pattern_copy)
        else:
            colors_copy = colors.copy()
            colors_copy[chosen_color] = False
            arrange_tiles(res, pattern_copy, colors_copy, m + 1)
