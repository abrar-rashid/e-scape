import random

import src.pages.pageTypes as pageTypes
from src.puzzle.generator import Generator, SeedMetadata
from wonderwords import RandomWord

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
filler_words = [
    "in",
    "around",
    "on",
    "to",
    "for",
    "until",
    "under",
    "upon",
    "towards",
    "inside",
    "during",
    "after",
    "before",
]


class NthLetter(Generator):

    def generate_puzzle(self):
        number_words = []
        for digit in str(self.solution):
            number_words.append(number_as_word[int(digit)])

        words = []

        random.seed(self.metadata.seed)

        n = random.randint(1, 5)
        for w in number_words:
            words.append(self.make_sentence(self.get_words(n, w)))

        puzzle = pageTypes.Content(
            type=pageTypes.ContentType.TEXT,
            content="\n".join(words),
        )

        hint1 = pageTypes.Content(
            type=pageTypes.ContentType.TEXT,
            content=f"""For all LETTERS in a word,
                                order must be preserved.
                                Meanings are hidden in POSITION,
                                of which {n+1} is reserved.""",
        )

        hint2 = pageTypes.Content(
            type=pageTypes.ContentType.TEXT,
            content="""In a place surrounded by malicious actors,
                your ability to isolate NOUNS will be the deciding factor.""",
        )

        return pageTypes.PuzzleInfo(
            mainPuzzle=puzzle, hints=[hint1, hint2])

    # Joins list of words together with filler words
    def make_sentence(self, words):
        sentence = []
        for i in range(len(words)):
            sentence.append(words[i])
            if i != len(words) - 1:
                sentence.append(random.choice(filler_words))
        return " ".join(sentence)

    # Returns list of words where the nth position is a letter from word

    def get_words(self, n, word):
        r = RandomWord()
        words = []
        for c in word:
            reg = r"\w{" + str(n) + "}" + c.lower() + r"\w*"
            words.append(
                r.word(regex=reg, word_min_length=n,
                       include_categories=["nouns"])
            )
        return words

    @classmethod
    def get_metadata(cls):
        return SeedMetadata
