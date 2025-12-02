import numpy as np

from test.dataclasses import ScorePlacementTestCase

PLACEMENT_SCORING_TEST_CASES = [
    ScorePlacementTestCase(
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
        m=2,
        n=2,
        expected=1,
    ),
    ScorePlacementTestCase(
        id="Horizontal Right Neighbor",
        wall=np.array(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
            dtype=bool,
        ),
        m=2,
        n=2,
        expected=2,
    ),
    ScorePlacementTestCase(
        id="Horizontal Both Sides",
        wall=np.array(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 1, 0, 1, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
            dtype=bool,
        ),
        m=2,
        n=2,
        expected=3,
    ),
    ScorePlacementTestCase(
        id="Horizontal Present But Not Adjacent 1",
        wall=np.array(
            [
                [0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [1, 1, 0, 0, 1],
                [1, 0, 0, 1, 0],
                [0, 0, 0, 0, 0],
            ],
            dtype=bool,
        ),
        m=2,
        n=2,
        expected=3,
    ),
    ScorePlacementTestCase(
        id="Horizontal Present But Not Adjacent 2",
        wall=np.array(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 1, 1],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
            dtype=bool,
        ),
        m=2,
        n=2,
        expected=3,
    ),
    ScorePlacementTestCase(
        id="Vertical Both Sides",
        wall=np.array(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
            ],
            dtype=bool,
        ),
        m=2,
        n=2,
        expected=3,
    ),
    ScorePlacementTestCase(
        id="Cross Shape Full Bonus",
        wall=np.array(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 1, 0, 1, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
            ],
            dtype=bool,
        ),
        m=2,
        n=2,
        expected=6,
    ),
    ScorePlacementTestCase(
        id="Edge Left Row Only",
        wall=np.array(
            [
                [0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
            ],
            dtype=bool,
        ),
        m=0,
        n=0,
        expected=2,
    ),
    ScorePlacementTestCase(
        id="Four In Row Start",
        wall=np.array(
            [
                [0, 1, 1, 1, 1],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
            dtype=bool,
        ),
        m=0,
        n=0,
        expected=5,
    ),
    ScorePlacementTestCase(
        id="Uneven Row And Column",
        wall=np.array(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 0, 0, 1, 0],
            ],
            dtype=bool,
        ),
        m=3,
        n=3,
        expected=5,
    ),
    ScorePlacementTestCase(
        id="Full Wall Center",
        wall=np.array(
            [
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 0, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
            ],
            dtype=bool,
        ),
        m=2,
        n=2,
        expected=10,
    ),
]
