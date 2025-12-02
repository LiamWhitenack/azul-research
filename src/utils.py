from src.permutations.pattern_lines import patternline_repr


def print_pattern_grid(grid):
    for row in grid:
        print(" ".join(patternline_repr(pl) for pl in row))
    print()
