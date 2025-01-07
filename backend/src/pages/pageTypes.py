from dataclasses import dataclass
from enum import Enum, IntEnum
from src.puzzle.generators.anagram import Anagram
from src.puzzle.generators.caesar import CaesarCipher
from src.puzzle.generators.connect_dots import ConnectDots
from src.puzzle.generators.cut_and_fold.cut_and_fold import CutAndFold
from src.puzzle.generators.steganograph import Steganograph
from os import listdir
from os.path import isfile, join
from src.puzzle.generators.jigsaw import Jigsaw
from src.puzzle.generators.maze import Maze
from src.puzzle.generators.mirror import Mirror
from src.puzzle.generators.morse_code import MorseCode
from src.puzzle.generators.nth_letter import NthLetter
from src.puzzle.generators.railroad_cipher import RailroadCipher
from src.puzzle.generators.skew import Skew
from src.puzzle.generators.word_search import WordSearch
from pathlib import Path
from PIL import Image

current_dir = Path(__file__).parent


class PageType(Enum):
    FRONT_NO_STORY = 0
    FRONT_WITH_STORY = 1
    PUZZLE_NO_STORY = 2
    PUZZLE_WITH_STORY = 3
    CONCLUSION = 4


def get_name(self):
    words = self.name.split('_')
    case_corrected = [word.capitalize() for word in words]
    return ' '.join(case_corrected)


class Theme(Enum):
    PIRATE = 1
    SPY = 2
    EGYPT = 3
    MEDIEVAL = 4

    def get_header_font(self):
        match self:
            case Theme.PIRATE:
                return (
                    "pirate_title_font",
                    f"{current_dir}/themes/pirate/fonts/pirate_title_font.ttf")
            case Theme.SPY:
                return (
                    "spy_title_font",
                    f"{current_dir}/themes/spy/fonts/spy_title.otf")
            case Theme.EGYPT:
                return (
                    "egypt_title_font",
                    f"{current_dir}/themes/egypt/fonts/egypt_title_font.ttf")
            case Theme.MEDIEVAL:
                return (
                    "medieval_title_font",
                    f"{current_dir}/themes/medieval/fonts/medieval_title_font.ttf")
            case _:
                return (
                    "general_title_font",
                    f"{current_dir}/themes/pirate/fonts/pirate_font_2.ttf")

    def get_body_font(self):
        match self:
            case Theme.PIRATE:
                return ("pirate_main_font",
                        f"{current_dir}/themes/pirate/fonts/pirate_font_2.ttf")
            case Theme.SPY:
                return ("spy_main_font",
                        f"{current_dir}/themes/spy/fonts/spy_main.ttf")
            case Theme.EGYPT:
                return (
                    "egypt_main_font",
                    f"{current_dir}/themes/egypt/fonts/egypt_main_font.ttf")
            case Theme.MEDIEVAL:
                return (
                    "medieval_main_font",
                    f"{current_dir}/themes/medieval/fonts/medieval_main_font.ttf")
            case _:
                return (
                    "general_main_font",
                    f"{current_dir}/themes/pirate/fonts/pirate_font_2.ttf")

    def get_papers(self):
        theme_dir = f"{current_dir}/themes/{str(self).lower()}/papers"
        return [join(theme_dir, f)
                for f in listdir(theme_dir) if isfile(join(theme_dir, f))]

    def get_graphics(self):
        theme_dir = f"{current_dir}/themes/{str(self).lower()}/graphics"
        return [join(theme_dir, f)
                for f in listdir(theme_dir) if isfile(join(theme_dir, f))]

    def __str__(self) -> str:
        match self:
            case Theme.PIRATE:
                return "Pirate"
            case Theme.SPY:
                return "Spy"
            case Theme.EGYPT:
                return "Egypt"
            case Theme.MEDIEVAL:
                return "Medieval"
            case _:
                return "Unknown"

    @classmethod
    def get_names(cls):
        return list(map(lambda c: get_name(Theme(c)), cls))

    def get_images(self):
        match self:
            case Theme.PIRATE:
                return 'images/pirate/'
            case Theme.SPY:
                return 'images/spy/'
            case Theme.EGYPT:
                return 'images/egypt/'
            case Theme.MEDIEVAL:
                return 'images/medieval/'


class Difficulty(IntEnum):
    EASY = 1
    MEDIUM = 2
    HARD = 3


class PuzzleType(Enum):
    CAESAR_CIPHER = 1
    MORSE_CODE = 2
    ANAGRAM = 3
    NTH_LETTER = 4
    WORD_SEARCH = 5
    JIGSAW = 6
    MAZE = 7
    SKEW = 8
    MIRROR = 9
    CUT_AND_FOLD = 10
    CONNECT_DOTS = 11
    STEGANOGRAPH = 12
    RAILROAD_CIPHER = 13

    @classmethod
    def as_set(cls):
        return set(map(lambda c: c.value, cls))

    @classmethod
    def get_names(cls):
        return list(map(lambda c: get_name(PuzzleType(c)), cls))

    def get_name(self):
        words = self.name.split('_')
        case_corrected = [word.capitalize() for word in words]
        return ' '.join(case_corrected)

    def get_difficulty(self):
        match self:
            case PuzzleType.CAESAR_CIPHER:
                return Difficulty.MEDIUM
            case PuzzleType.MORSE_CODE:
                return Difficulty.EASY
            case PuzzleType.ANAGRAM:
                return Difficulty.EASY
            case PuzzleType.NTH_LETTER:
                return Difficulty.MEDIUM
            case PuzzleType.WORD_SEARCH:
                return Difficulty.HARD
            case PuzzleType.JIGSAW:
                return Difficulty.EASY
            case PuzzleType.MAZE:
                return Difficulty.MEDIUM
            case PuzzleType.SKEW:
                return Difficulty.EASY
            case PuzzleType.MIRROR:
                return Difficulty.EASY
            case PuzzleType.CUT_AND_FOLD:
                return Difficulty.MEDIUM
            case PuzzleType.CONNECT_DOTS:
                return Difficulty.MEDIUM
            case PuzzleType.STEGANOGRAPH:
                return Difficulty.EASY
            case PuzzleType.RAILROAD_CIPHER:
                return Difficulty.MEDIUM

    def get_generator(self):
        match self:
            case PuzzleType.ANAGRAM:
                return Anagram
            case PuzzleType.CAESAR_CIPHER:
                return CaesarCipher
            case PuzzleType.JIGSAW:
                return Jigsaw
            case PuzzleType.MAZE:
                return Maze
            case PuzzleType.MORSE_CODE:
                return MorseCode
            case PuzzleType.NTH_LETTER:
                return NthLetter
            case PuzzleType.WORD_SEARCH:
                return WordSearch
            case PuzzleType.SKEW:
                return Skew
            case PuzzleType.MIRROR:
                return Mirror
            case PuzzleType.CUT_AND_FOLD:
                return CutAndFold
            case PuzzleType.CONNECT_DOTS:
                return ConnectDots
            case PuzzleType.STEGANOGRAPH:
                return Steganograph
            case PuzzleType.RAILROAD_CIPHER:
                return RailroadCipher


class AspectRatio(Enum):
    DEFAULT = 1
    # TODO: Define these properly
    pass


class ContentType(Enum):
    IMAGE = 1
    TEXT = 2


@dataclass
class Content:
    type: ContentType
    content: Image.Image | str


@dataclass
class PuzzleInfo:
    mainPuzzle: Content
    hints: list[Content]


@dataclass
class PageMetadata:
    title: str
    number: int
    content: Content
    hintOne: Content
    hintTwo: Content


@dataclass
class Font:
    path: str
    size: int
    colour: str


@dataclass
class Vector2d:
    x: int
    y: int


@dataclass
class Position:
    xScale: float
    xOffset: int
    yScale: float
    yOffset: int


@dataclass
class ContentFrame:
    position: Position
    aspectRatio: AspectRatio


@dataclass
class TemplateMetadata:
    background: str
    titleFont: Font
    titlePosition: Position
    pageNumberPosition: Position
    mainFont: Font

    puzzleFrame: ContentFrame
    hintOneFrame: ContentFrame
    hintTwoFrame: ContentFrame
