import numpy as np
from colorama import Fore, Style
from numba import int8
from numba.experimental import jitclass

spec = [
    ("count", int8),
    ("color", int8),
    ("potential_colors", int8[:]),
]


@jitclass(spec)  # type: ignore
class PatternLine:
    def __init__(self) -> None:
        self.count = 0
        self.color = -1
        self.potential_colors = np.arange(5, dtype=np.int8)

    def copy(self):
        new_obj = PatternLine()
        new_obj.count = self.count
        new_obj.color = self.color
        new_obj.potential_colors = self.potential_colors.copy()
        return new_obj


PatternLines = list[PatternLine]


def patternline_repr(pl: PatternLine) -> str:
    if pl.color == -1:
        color_str = f"{Style.DIM}[none]{Style.RESET_ALL}"
    else:
        # Map tile index to a color
        palette = [
            Fore.RED,
            Fore.GREEN,
            Fore.YELLOW,
            Fore.BLUE,
            Fore.MAGENTA,
        ]
        ansi = palette[pl.color]
        color_str = f"{ansi}{pl.count}{Style.RESET_ALL}"

    return color_str


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
