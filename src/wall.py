from typing import Annotated

import numpy as np
from numpy.typing import NDArray

WallType = Annotated[NDArray[np.bool_], (5, 5)]


def empty_wall() -> WallType:
    return np.array(
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ],
        dtype=bool,
    )
