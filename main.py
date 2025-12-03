from time import perf_counter

import numpy as np

from src.permutations.all_scores import get_all_scores
from src.permutations.arrangements import all_placements
from src.permutations.pattern_lines import TestingPatternLine
from src.pickle_path import save_progression
from src.utils import print_pattern_grid
from src.view_progression import make_grid, print_grids

g1 = make_grid(1)
g2 = make_grid(2)
g3 = make_grid(3)
g4 = make_grid(4)
g5 = make_grid(5)

print("\n--- SIDE BY SIDE ---")
print_grids([g1, g2, g3, g4, g5], orientation="horizontal")

print("\n--- VERTICAL ---")
print_grids([g1, g2, g3, g4, g5], orientation="vertical")

experiment = "2 by 5 nullable when necessary"
start = perf_counter()
scores = get_all_scores()

save_progression(
    max(scores, key=lambda x: x[0]),
    f"pickles/{experiment}_{round(perf_counter() - start, 3)}".replace(
        ".", "_"
    ).replace(" ", "_")
    + ".pkl",
)
pass
