import pickle
from pathlib import Path
from typing import TypeVar

from src.permutations.pattern_lines import PatternLines
from src.wall import WallType

T = TypeVar("T")


def save_progression(
    progression: tuple[int, list[PatternLines], WallType],
    path: str | Path,
    protocol: int = pickle.HIGHEST_PROTOCOL,
) -> None:
    path = Path(path)
    with path.open("wb") as f:
        pickle.dump(progression, f, protocol=protocol)


def load_progression(path: str | Path) -> tuple[int, list[PatternLines], WallType]:
    path = Path(path)
    with path.open("rb") as f:
        return pickle.load(f)
