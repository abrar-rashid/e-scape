from src.puzzle.generator import Generator, SeedMetadata
import src.pages.pageTypes as pageTypes
import random

number_as_word = [
    "ZERO",
    "ONE",
    "TWO",
    "THREE",
    "FOUR",
    "FIVE",
    "SIX",
    "SEVEN",
    "EIGHT",
    "NINE",
]


class Anagram(Generator):

    def generate_puzzle(self):

        number_words = []  # e.g. ["ONE", "TWO", "THREE", "FOUR"]
        for digit in str(self.solution):
            number_words.append(number_as_word[int(digit)])

        random.seed(self.metadata.seed)
        anagram_list = []
        for word in number_words:
            char_list = list(word)
            while "".join(char_list) == word:
                random.shuffle(char_list)
            anagram_list.append("".join(char_list))

        puzzle = pageTypes.Content(
            type=pageTypes.ContentType.TEXT,
            content="\n".join(anagram_list),
        )

        hint1 = pageTypes.Content(
            type=pageTypes.ContentType.TEXT,
            content="Seek out a hidden message nestled within these letters.",
        )

        hint2 = pageTypes.Content(
            type=pageTypes.ContentType.TEXT,
            content="",
        )

        return pageTypes.PuzzleInfo(
            mainPuzzle=puzzle, hints=[hint1, hint2])

    @classmethod
    def get_metadata(cls):
        return SeedMetadata
