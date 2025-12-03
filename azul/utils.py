import time
from functools import wraps

from azul.permutations.pattern_lines import patternline_repr


def print_pattern_grid(grid):
    for row in grid:
        print(" ".join(patternline_repr(pl) for pl in row))
    print()


def timed(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            return fn(*args, **kwargs)
        finally:
            end = time.perf_counter()
            duration = end - start
            print(f"{fn.__name__} took {duration:.6f}s")

    return wrapper
