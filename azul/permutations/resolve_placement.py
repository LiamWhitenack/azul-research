import numpy as np

from azul.permutations.pattern_lines import PatternLines, TestingPatternLine
from azul.score import score_placement
from azul.types import WallType


def resolve_placement(
    score: int, path: list[PatternLines], wall: WallType
) -> tuple[int, list[PatternLines], WallType]:
    line: TestingPatternLine
    for m, line in enumerate(path[-1]):
        if line.count > m:
            score += score_placement(wall.copy(), m, line.color)
            wall[m, line.color] = True
            line.potential_colors[line.color] = False
            line.color = -1
            line.count = 0
    if np.sum(wall) < 2:
        pass

    return score, path, wall
