import io
import src.pages.pageTypes as pageTypes
from src.puzzle.generator import Generator, SeedMetadata
from svgwrite import Drawing
import random
import string
import cairosvg

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


class WordSearch(Generator):

    def genearate_grid(self):
        number_words = [number_as_word[int(digit)]
                        for digit in str(self.solution)]
        size = 12
        grid = [[" " for _ in range(size)] for _ in range(size)]
        random.seed(self.metadata.seed)

        for word in number_words:
            placed = False
            attempts = 0

            while not placed and attempts < 10:
                direction = random.choice(
                    [(1, 0), (0, 1), (1, 1), (-1, 1)])
                x, y = random.randint(
                    0, size - 1), random.randint(0, size - 1)

                # check if the word fits in the grid in the chosen
                # direction
                if (
                    0 <= x + len(word) * direction[0] < size
                    and 0 <= y + len(word) * direction[1] < size
                ):
                    # check if there's any overlap with existing letters
                    overlap = False
                    for i, letter in enumerate(word):
                        if grid[x + i * direction[0]
                                ][y + i * direction[1]] != " ":
                            overlap = True
                            break
                    if not overlap:
                        # place the word in the grid
                        for i, letter in enumerate(word):
                            grid[x + i * direction[0]
                                 ][y + i * direction[1]] = letter
                        placed = True
                attempts += 1
                print(
                    f"Number: {word}, Attempt: {attempts}, Placed: {placed}")

        # fill remaining empty spaces with random letters
        for i in range(size):
            for j in range(size):
                if grid[i][j] == " ":
                    grid[i][j] = random.choice(string.ascii_uppercase)

        return grid

    def create_image(self):
        grid = self.genearate_grid()
        margin = 20
        print(self.solution)
        img_path = "wordsearch_img.svg"
        dwg = Drawing(
            filename=img_path, size=(f"{400}px", f"{400}px"))

        for i, row in enumerate(grid):
            for j, letter in enumerate(row):
                x = margin + i * (10 + margin)
                y = margin + j * (10 + margin)

                dwg.add(dwg.text(
                    letter, insert=(f"{x+4}px", f"{y-5}px"),
                    fill="black", font_size="15px"))

        string_buffer = io.StringIO()

        dwg.write(string_buffer)

        svg_string = string_buffer.getvalue()

        img = io.BytesIO()
        cairosvg.svg2png(bytestring=svg_string, write_to=img)

        return img

    def generateHint2(self):
        letters = ['A', 'B', 'C', 'D', 'E', 'F']
        digits = [int(digit) for digit in str(self.solution)]
        sorted_number = list(set(sorted(digits)))

        result = ""
        for n in str(self.solution):
            result += letters[sorted_number.index(int(n))]

        return f"""The ordering of the secret code resembles the ordering of
          {result}"""

    def generate_puzzle(self):
        image_path = self.create_image()

        puzzle = pageTypes.Content(
            type=pageTypes.ContentType.IMAGE,
            content=image_path
        )

        hint1 = pageTypes.Content(
            type=pageTypes.ContentType.TEXT,
            content=f"""Discover a concealed code of length {
                len(str(self.solution))
                }
                within these letters.""", )

        hint2 = pageTypes.Content(
            type=pageTypes.ContentType.TEXT,
            content=self.generateHint2()
        )

        return pageTypes.PuzzleInfo(
            mainPuzzle=puzzle, hints=[hint1, hint2])

    def format_grid(self, grid):
        rows = []
        for row in grid:
            rows.append(" ".join(row))
        return "<br/><br/>".join(rows)

    @classmethod
    def get_metadata(cls):
        return SeedMetadata
