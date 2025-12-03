from collections import Counter
from time import perf_counter

import matplotlib.pyplot as plt
import numpy as np

from azul.permutations.all_scores import get_all_scores
from azul.permutations.arrangements import all_placements
from azul.permutations.pattern_lines import NumbaPatternLine
from azul.pickle_progression import save_progression
from azul.view_progression import (
    make_grids,
    styled_grid_progression,
)

experiment = "2 by 5 nullable when necessary"
optimization_method = "no optimization"
start = perf_counter()
scores = get_all_scores(n_rounds=5)

data = [score[0] for score in scores]
hist, bins = np.histogram(data, bins=range(min(data), max(data) + 2))
plt.bar(bins[:-1], hist, width=0.8, edgecolor="black")
# plt.show()

best_progression = max(scores, key=lambda x: x[0])

print(styled_grid_progression(best_progression, style="print"))
# save_progression(
#     best_progression,
#     f"pickles/{experiment} {round(perf_counter() - start, 3)} {optimization_method}".replace(
#         ".", "_"
#     ).replace(" ", "_")
#     + ".pkl",
# )
pass
