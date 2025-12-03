from time import perf_counter

import numpy as np

from pickle_path import save_progression
from src.permutations.all_scores import get_all_scores
from src.permutations.arrangements import all_placements
from src.permutations.pattern_lines import TestingPatternLine
from src.utils import print_pattern_grid

experiment = "perfect_score"
start = perf_counter()
scores = get_all_scores()


save_progression(
    max(scores, key=lambda x: x[0]),
    f"{experiment}_{perf_counter() - start}".replace(".", "_") + ".pkl",
)
pass
