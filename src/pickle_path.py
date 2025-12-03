import pickle
from pathlib import Path
from typing import TypeVar

from src.permutations.pattern_lines import PatternLines
from src.types import GameProgression, WallType

T = TypeVar("T")


def save_progression(
    progression: GameProgression,
    path: str | Path,
    protocol: int = pickle.HIGHEST_PROTOCOL,
) -> None:
    path = Path(path)
    with path.open("wb") as f:
        pickle.dump(progression, f, protocol=protocol)


def load_progression(path: str | Path) -> GameProgression:
    path = Path(path)
    with path.open("rb") as f:
        return pickle.load(f)
