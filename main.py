import numpy as np

from src.permutations import PatternLine, all_placements, patternline_repr


def print_pattern_grid(grid):
    for row in grid:
        print(" ".join(patternline_repr(pl) for pl in row))
    print()


print_pattern_grid(all_placements([PatternLine() for _ in range(5)]))
