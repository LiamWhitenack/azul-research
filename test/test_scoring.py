import pytest

from azul.score import score_endgame, score_placement
from test.cases.endgame_scoring import ENDGAME_SCORING_TEST_CASES
from test.cases.placement_scoring import PLACEMENT_SCORING_TEST_CASES
from test.dataclasses import ScoreEndgameTestCase, ScorePlacementTestCase


@pytest.mark.parametrize(
    "case",
    PLACEMENT_SCORING_TEST_CASES,
    ids=[c.id for c in PLACEMENT_SCORING_TEST_CASES],
)
def test_placement_scoring(case: ScorePlacementTestCase):
    result = score_placement(case.wall, case.m, case.n)
    assert result == case.expected, f"{case.id}: expected {case.expected}, got {result}"


@pytest.mark.parametrize(
    "case",
    ENDGAME_SCORING_TEST_CASES,
    ids=[c.id for c in ENDGAME_SCORING_TEST_CASES],
)
def test_endgame_scoring(case: ScoreEndgameTestCase):
    result = score_endgame(case.wall)
    assert result == case.expected, f"{case.id}: expected {case.expected}, got {result}"
