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
