from guidance import assistant, gen, models, system
from openai import OpenAI
from src.pages.pageTypes import Difficulty, PuzzleType, Theme

client = OpenAI()

gpt = models.OpenAI("gpt-3.5-turbo")


class Content:
    def __init__(self):
        None


def matchTheme(theme):
    match theme:
        case Theme.PIRATE:
            return "pirates "
    return


def matchDifficulty(difficulty):
    match difficulty:
        case Difficulty.KIDS:
            return "an easy "


# constraint satisfaction problem
def create_puzzle_csp(theme, difficulty):

    context = """Generate """
    context += matchDifficulty(difficulty)
    context += """constraint-restriction puzzle with theme """
    context += matchTheme(theme)
    context += """where the answer must be a sequence of 6 digits and
     every digit is under 10. """

    return context


def create_puzzle(theme, difficulty, puzzle_type):
    # return puzzle, hints and answer to puzzle (int for now) and aspect ratio?
    # adds contents of the puzzle to the puzzle
    match puzzle_type:
        case PuzzleType.CSP:
            return create_puzzle_csp(theme, difficulty)
    return


# would we need separate generate contents for different types of puzzles?
def generate_content(theme, difficulty, description, puzzle_type):
    # generates content of the puzzle e.g. if it's a crossword, it returns word
    # generate and return puzzle contents, list of hints and puzzle answer
    # (should be stored somewhere)

    context = create_puzzle(theme, difficulty, puzzle_type)

    context += """After generating this puzzle, work out the
     solution to the puzzle."""

    with system():
        txt = gpt + context
    with assistant():
        txt += gen()

    return txt


# optional
# def generate_description(theme, keywords):
#     return


def generate_hints(puzzle):
    return


# if __name__ == "__main__":
# puzzle, hints = create_puzzle()
# generate_content(Theme.PIRATE, Difficulty.KIDS, "", PuzzleType.CSP)


# need to return puzzle flowable and hints flowable to template
