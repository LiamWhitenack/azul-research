import numpy as np

from src.permutations.pattern_lines import PatternLines, TestingPatternLine
from src.score import score_placement
from src.types import WallType


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
