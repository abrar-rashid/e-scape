import src.pages.pageTypes as pageTypes
from src.puzzle.generator import Generator, NoneMetadata


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

MORSE_CODE_DICT_LETTERS = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
}

# MORSE_CODE_DICT_LETTERS_1 = { 'A':'.-', 'B':'-...',
#                     'C':'-.-.', 'D':'-..', 'E':'.',
#                     'F':'..-.', 'G':'--.', 'H':'....',
#                     'I':'..', 'J':'.---', 'K':'-.-',
#                     'L':'.-..', 'M':'--'}

# MORSE_CODE_DICT_LETTERS_2 = {'N':'-.',
#                     'O':'---', 'P':'.--.', 'Q':'--.-',
#                     'R':'.-.', 'S':'...', 'T':'-',
#                     'U':'..-', 'V':'...-', 'W':'.--',
#                     'X':'-..-', 'Y':'-.--', 'Z':'--..'}

MORSE_CODE_DIGITS = {
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}

MORSE_CODE_SYMBOLS = {
    ", ": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
}


class MorseCode(Generator):

    def print_dict(self, dict):
        formatted_dict = ""
        i = 1
        for key, value in dict.items():
            formatted_dict += "{}: {}  ".format(key, value)
            if i % 3 == 0:
                formatted_dict += "\n"
            i += 1
        return formatted_dict

    def generate_puzzle(self):
        number_words = []
        for word in str(self.solution):
            number_words.append(number_as_word[int(word)])

        morse_code_str = ""
        for word in number_words:
            for letter in word:
                morse_code_str += MORSE_CODE_DICT_LETTERS[letter]
                morse_code_str += " "
            morse_code_str += '\n'

        puzzle = pageTypes.Content(
            type=pageTypes.ContentType.TEXT,
            content=morse_code_str,
        )

        key_1 = self.print_dict(
            dict(
                list(MORSE_CODE_DICT_LETTERS.items())[
                    : len(MORSE_CODE_DICT_LETTERS) // 2
                ]
            )
        )
        key_2 = self.print_dict(
            dict(
                list(MORSE_CODE_DICT_LETTERS.items())[
                    len(MORSE_CODE_DICT_LETTERS) // 2:
                ]
            )
        )
        hint1 = pageTypes.Content(
            type=pageTypes.ContentType.TEXT,
            content=key_1,
        )

        hint2 = pageTypes.Content(
            type=pageTypes.ContentType.TEXT,
            content=key_2,
        )

        return pageTypes.PuzzleInfo(
            mainPuzzle=puzzle, hints=[hint1, hint2])

    @classmethod
    def get_metadata(cls):
        return NoneMetadata
