import io
import src.pages.pageTypes as pageTypes
from src.puzzle.generator import Generator, NoneMetadata
from svgwrite import Drawing
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


class RailroadCipher(Generator):

    def generate_grid(self):
        letters = ''.join([number_as_word[int(i)] for i in str(self.solution)])

        if len(letters) % 3 == 1:
            letters = 'X' + letters + 'X'
        elif len(letters) % 3 == 2:
            letters += 'X'

        grid = []
        for i in range(0, len(letters), 3):
            grid.append([letters[i], letters[i + 1], letters[i + 2]])

        for i, row in enumerate(grid):
            if i % 2 == 1:
                grid[i] = grid[i][::-1]

        grid = [[row[i] for row in grid] for i in range(len(grid[0]))]

        for row in grid:
            print(row)

        return grid

    def create_image(self):
        grid = self.generate_grid()
        margin = 25
        img_path = "railroad_cipher.svg"
        dwg = Drawing(
            filename=img_path, size=(450, 300))

        for i, row in enumerate(grid):
            for j, letter in enumerate(row):
                y = margin + i * (10 + margin)
                x = margin + j * (10 + margin)

                dwg.add(dwg.text(
                    letter, insert=(x, y),
                    fill="black", font_size="25px"))

        string_buffer = io.StringIO()

        dwg.write(string_buffer)

        svg_string = string_buffer.getvalue()

        img = io.BytesIO()
        cairosvg.svg2png(bytestring=svg_string, write_to=img)

        return img

    def generate_puzzle(self):
        image_path = self.create_image()

        puzzle = pageTypes.Content(
            type=pageTypes.ContentType.IMAGE,
            content=image_path
        )

        hint1 = pageTypes.Content(
            type=pageTypes.ContentType.TEXT,
            content="Zigzag patters will guide you."
        )

        hint2 = pageTypes.Content(
            type=pageTypes.ContentType.TEXT,
            content=""
        )

        return pageTypes.PuzzleInfo(
            mainPuzzle=puzzle, hints=[hint1, hint2]
        )

    @classmethod
    def get_metadata(cls):
        return NoneMetadata
