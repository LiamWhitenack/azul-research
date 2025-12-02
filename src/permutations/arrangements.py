import numpy as np

from permutations.pattern_lines import PatternLines


def all_placements(input: PatternLines) -> list[PatternLines]:
    placements: list[PatternLines] = []
    arrange_tiles(placements, input)
    return placements


def arrange_tiles(
    res: list[PatternLines],
    pattern: PatternLines,
    colors: np.ndarray = np.ones(5, dtype=np.bool_),  # instead of set(range(5))
    m: int = 0,
) -> None:
    line = pattern[m]

    # line.potential_colors is an array of int8 (e.g., [0,1,2,3,4])
    # Create mask: True where color is allowed by line AND still available
    compatible_colors = np.zeros(5, dtype=np.bool_)
    compatible_colors[line.potential_colors] = True
    compatible_colors &= colors  # elementwise AND, replaces set.union

    # While any color is still compatible
    while compatible_colors.any():
        pattern_copy = pattern.copy()
        line_copy = line.copy()

        # Pick one available color (equivalent to popping from a set)
        chosen_color = int(np.argmax(compatible_colors))
        compatible_colors[chosen_color] = False  # remove it

        line_copy.color = chosen_color
        line_copy.count += 2
        pattern_copy[m] = line_copy

        if m == 4:
            res.append(pattern_copy)
        else:
            # Copy color mask for recursion
            colors_copy = colors.copy()
            colors_copy[chosen_color] = False
            arrange_tiles(res, pattern_copy, colors_copy, m + 1)
