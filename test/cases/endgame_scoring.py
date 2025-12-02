import numpy as np

from test.dataclasses import ScoreEndgameTestCase

ENDGAME_SCORING_TEST_CASES = [
    ScoreEndgameTestCase(
        id="Empty Wall Single Tile",
        wall=np.array(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
            dtype=bool,
        ),
        expected=0,
    ),
    ScoreEndgameTestCase(
        id="Row",
        wall=np.array(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
            dtype=bool,
        ),
        expected=2,
    ),
    ScoreEndgameTestCase(
        id="Rows",
        wall=np.array(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1],
            ],
            dtype=bool,
        ),
        expected=4,
    ),
    ScoreEndgameTestCase(
        id="Column",
        wall=np.array(
            [
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1],
            ],
            dtype=bool,
        ),
        expected=7,
    ),
    ScoreEndgameTestCase(
        id="Standard Diagonal",
        wall=np.array(
            [
                [1, 0, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 0, 1, 1, 0],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1],
            ],
            dtype=bool,
        ),
        expected=10,
    ),
    ScoreEndgameTestCase(
        id="Tough Diagonal 1",
        wall=np.array(
            [
                [1, 1, 0, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 1, 1],
                [1, 0, 0, 0, 1],
            ],
            dtype=bool,
        ),
        expected=20,
    ),
    ScoreEndgameTestCase(
        id="Tough Diagonal 2",
        wall=np.array(
            [
                [1, 1, 0, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 1, 1],
                [0, 0, 0, 0, 1],
            ],
            dtype=bool,
        ),
        expected=10,
    ),
    ScoreEndgameTestCase(
        id="Full",
        wall=np.array(
            [
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
            ],
            dtype=bool,
        ),
        expected=10 + 35 + 50,
    ),
]
