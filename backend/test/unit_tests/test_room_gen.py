import environment  # NOQA isort:skip
import pytest
from src.pages.pageTypes import Difficulty, PuzzleType, Theme
from src.room_new import Room


def test_generate_escape_room_valid_parameters():
    a = [x for x in PuzzleType]
    room = Room(Theme.PIRATE, ["finding buried treasure",
                "exploring the seas"], Difficulty.HARD,
                len(a), a, [], include_storyline=False)
    pdf_path = room.create_room()
    assert pdf_path is not None


def test_generate_escape_room_invalid_theme():
    a = [x for x in PuzzleType]
    with pytest.raises(TypeError):
        Room(1, ["finding buried treasure",
             "exploring the seas"], Difficulty.HARD,
             len(a), a, [], include_storyline=False)


def test_generate_escape_room_invalid_difficulty():
    a = [x for x in PuzzleType]
    with pytest.raises(TypeError):
        Room(Theme.PIRATE, ["finding buried treasure",
             "exploring the seas"], 3,
             len(a), a, [], include_storyline=False)
