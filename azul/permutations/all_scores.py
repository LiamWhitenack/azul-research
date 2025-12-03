from azul.permutations.arrangements import all_placements
from azul.permutations.pattern_lines import NumbaPatternLine, PatternLines
from azul.permutations.resolve_placement import resolve_placement
from azul.score import score_endgame
from azul.types import GameProgression, WallType
from azul.utils import timed
from azul.wall import empty_wall


@timed
def get_all_scores(
    starting_score: int = 0,
    path: list[PatternLines] = [[NumbaPatternLine() for _ in range(5)]],
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
