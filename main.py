from time import perf_counter

import numpy as np

from src.permutations.all_scores import get_all_scores
from src.permutations.arrangements import all_placements
from src.permutations.pattern_lines import TestingPatternLine
from src.pickle_path import save_progression
from src.utils import print_pattern_grid
from src.view_progression import make_grids, print_grids

experiment = "2 by 5 nullable when necessary"
start = perf_counter()
scores = get_all_scores(n_rounds=5)
best_progression = min(scores, key=lambda x: x[0])

print_grids(make_grids(best_progression), orientation="horizontal")
save_progression(
    best_progression,
    f"pickles/{experiment}_{round(perf_counter() - start, 3)}".replace(
        ".", "_"
    ).replace(" ", "_")
    + ".pkl",
)
pass
