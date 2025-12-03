from typing import Annotated

import numpy as np
from numpy.typing import NDArray

from azul.permutations.pattern_lines import PatternLines

WallType = Annotated[NDArray[np.bool_], (5, 5)]
GameProgression = tuple[int, list[PatternLines], WallType]
