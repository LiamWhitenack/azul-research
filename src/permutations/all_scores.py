from src.permutations.arrangements import all_placements
from src.permutations.pattern_lines import PatternLine, PatternLines
from src.permutations.resolve_placement import resolve_placement
from src.wall import WallType, empty_wall


def get_all_scores() -> list[tuple[int, list[PatternLines], WallType]]:
    res: list[tuple[int, list[PatternLines], WallType]] = []
    unfinished: list[tuple[int, list[PatternLines], WallType]] = [
        (0, [[PatternLine() for _ in range(5)]], empty_wall())
    ]
    while unfinished:
        score, path, wall = unfinished.pop(0)
        if len(path) == 2:
            res.append((score, path, wall))
            continue
        for pattern_lines in all_placements(path[-1]):
            res.append(
                resolve_placement(score=score, path=path + [pattern_lines], wall=wall)
            )

    return res
