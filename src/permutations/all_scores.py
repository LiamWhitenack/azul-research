from src.permutations.arrangements import all_placements
from src.permutations.pattern_lines import PatternLines, TestingPatternLine
from src.permutations.resolve_placement import resolve_placement
from src.wall import WallType, empty_wall


def get_all_scores() -> list[tuple[int, list[PatternLines], WallType]]:
    res: list[tuple[int, list[PatternLines], WallType]] = []
    unfinished: list[tuple[int, list[PatternLines], WallType]] = [
        (0, [[TestingPatternLine() for _ in range(5)]], empty_wall())
    ]
    while unfinished:
        score, path, wall = unfinished.pop(0)
        if len(path) == 5:
            res.append((score, path, wall))
            continue
        # if len(path) == 6:
        #     pass
        for pattern_lines in all_placements(path[-1]):
            unfinished.append(
                resolve_placement(
                    score=score, path=path + [pattern_lines], wall=wall.copy()
                )
            )

    return res
