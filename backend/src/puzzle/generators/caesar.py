import random
from dataclasses import dataclass
from src.puzzle.generator import Generator, Metadata
import src.pages.pageTypes as pageTypes

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


@dataclass
class CaesarCipherMetadata(Metadata):
    shift: int

    @classmethod
    def get_random(cls):
        return cls(random.randint(1, 25))


class CaesarCipher(Generator):

    def generate_puzzle(self):
        number = []
        for digit in str(self.solution):
            number.append(number_as_word[int(digit)])
        shifted_number = []
        for word in number:
            shifted_number.append(self.shift_word(word))

        puzzle = pageTypes.Content(
            type=pageTypes.ContentType.TEXT,
            content="\n".join(shifted_number)
        )

        hint1 = pageTypes.Content(
            type=pageTypes.ContentType.TEXT,
            content=f"""The great Roman Emperor was always
                                {self.metadata.shift} steps ahead."""
        )

        hint2 = pageTypes.Content(
            type=pageTypes.ContentType.TEXT,
            content="",
        )

        return pageTypes.PuzzleInfo(
            mainPuzzle=puzzle, hints=[hint1, hint2])

    def shift_word(self, word):
        shifted_word = []
        for letter in word:
            shifted_letter_ord = (
                ((ord(letter) - ord("A")) + self.metadata.shift) % 26
            ) + ord("A")
            shifted_letter = chr(shifted_letter_ord)
            shifted_word.append(shifted_letter)

        return "".join(shifted_word)

    @classmethod
    def get_metadata(cls):
        return CaesarCipherMetadata
