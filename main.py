from time import perf_counter

import numpy as np

from src.permutations.all_scores import get_all_scores
from src.permutations.arrangements import all_placements
from src.permutations.pattern_lines import TestingPatternLine
from src.pickle_progression import save_progression
from src.utils import print_pattern_grid
from src.view_progression import (
    make_grids,
    styled_grid_progression,
)

experiment = "2 by 5 nullable when necessary"
optimization_method = "no optimization"
start = perf_counter()
scores = get_all_scores(n_rounds=4)
best_progression = max(reversed(scores), key=lambda x: x[0])

with open("test.md", "w") as f:
    f.writelines(styled_grid_progression(best_progression, style="markdown"))
print(styled_grid_progression(best_progression, style="print"))
save_progression(
    best_progression,
    f"pickles/{experiment} {round(perf_counter() - start, 3)} {optimization_method}".replace(
        ".", "_"
    ).replace(" ", "_")
    + ".pkl",
)
pass
