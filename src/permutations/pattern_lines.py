import numpy as np
from colorama import Fore, Style
from numba import bool_, boolean, int8, types
from numba.experimental import jitclass

spec = [
    ("count", int8),
    ("color", int8),
    ("potential_colors", types.Array(boolean, 1, "C")),
]


@jitclass(spec)  # type: ignore
class PatternLine:
    def __init__(self):
        self.count = 0
        self.color = -1
        # Must allocate array inside __init__
        self.potential_colors = np.ones(5, dtype=np.bool_)

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
