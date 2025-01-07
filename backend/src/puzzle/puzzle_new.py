from guidance import models
from openai import OpenAI
from src.pages.pageTypes import PuzzleType
from src.puzzle.generators.anagram import Anagram
from src.puzzle.generators.caesar import CaesarCipher
from src.puzzle.generators.cut_and_fold.cut_and_fold import CutAndFold
from src.puzzle.generators.steganograph import Steganograph
from src.puzzle.generators.jigsaw import Jigsaw
from src.puzzle.generators.maze import Maze
from src.puzzle.generators.morse_code import MorseCode
from src.puzzle.generators.nth_letter import NthLetter
from src.puzzle.generators.word_search import WordSearch

client = OpenAI()

gpt = models.OpenAI("gpt-3.5-turbo")


# class PuzzleType(Enum):
#     CSP = 1
#     CAESAR_CIPHER = 2


def create_puzzle(theme, difficulty, puzzle_type, solution, seed):
    metadata = PuzzleType.get_metadata(puzzle_type)(seed)
    match puzzle_type:
        # case PuzzleType.CSP:
        #     return create_puzzle_csp()
        case PuzzleType.CAESAR_CIPHER:
            return CaesarCipher(solution, metadata).generate_puzzle()
        case PuzzleType.MORSE_CODE:
            return MorseCode(solution).generate_puzzle()
        case PuzzleType.ANAGRAM:
            return Anagram(solution, metadata).generate_puzzle()
        case PuzzleType.NTH_LETTER:
            return NthLetter(solution, metadata).generate_puzzle()
        case PuzzleType.WORD_SEARCH:
            return WordSearch(solution, metadata).generate_puzzle()
        case PuzzleType.JIGSAW:
            return Jigsaw(solution, metadata).generate_puzzle()
        case PuzzleType.MAZE:
            return Maze(solution, metadata).generate_puzzle()
        case PuzzleType.CUT_AND_FOLD:
            return CutAndFold(solution, metadata).generate_puzzle()
        case PuzzleType.STEGANOGRAPH:
            return Steganograph(solution, metadata).generate_puzzle()
