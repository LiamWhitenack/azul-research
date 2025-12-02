from src.permutations.pattern_lines import PatternLine, PatternLines
from src.score import score_placement
from src.wall import WallType


def resolve_placement(
    score: int, path: list[PatternLines], wall: WallType
) -> tuple[int, list[PatternLines], WallType]:
    line: PatternLine
    for m, line in enumerate(path[-1]):
        if line.count > m:
            score += score_placement(wall, m, line.color)
            line.potential_colors[line.color] = False
            line.color = -1
            line.count = 0
            wall[m, line.color] = True

    return score, path, wall
