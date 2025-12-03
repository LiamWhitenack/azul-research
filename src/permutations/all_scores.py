from src.permutations.arrangements import all_placements
from src.permutations.pattern_lines import PatternLines, TestingPatternLine
from src.permutations.resolve_placement import resolve_placement
from src.score import score_endgame
from src.types import GameProgression, WallType
from src.utils import timed
from src.wall import empty_wall


@timed
def get_all_scores(
    starting_score: int = 0,
    path: list[PatternLines] = [[TestingPatternLine() for _ in range(5)]],
    wall: WallType = empty_wall(),
    n_rounds: int = 5,
) -> list[GameProgression]:
    res: list[GameProgression] = []
    unfinished: list[GameProgression] = [(starting_score, path, wall)]
    while unfinished:
        score, path, wall = unfinished.pop(0)
        if len(path) == n_rounds + 1:
            score += score_endgame(wall)
            res.append((score, path, wall))
            continue
        # if len(path) == 6:
        #     pass
        for pattern_lines in all_placements(path[-1]):
            unfinished.append(
                resolve_placement(
                    score=score,
                    path=path + [[line.copy() for line in pattern_lines]],
                    wall=wall.copy(),
                )
            )

    return res
