from src.puzzle.generator import Generator, SeedMetadata
import src.pages.pageTypes as pageTypes
import cv2
import numpy as np
from PIL import Image
import random
from pathlib import Path

cur_dir = Path(__file__).parent


class Jigsaw(Generator):

    def create_image(self):
        # no return since it'll eventually be stored in a database?
        img = np.zeros((350, 725, 3), dtype=np.uint8)
        img.fill(255)
        cv2.rectangle(img, (25, 25), (700, 325), (0, 0, 0), 2)
        cv2.putText(
            img, str("CODE IS"),
            (30, 150),
            cv2.FONT_HERSHEY_TRIPLEX, 5, (0, 0, 0),
            2)
        cv2.putText(
            img,
            str(self.solution),
            (55, 300),
            cv2.FONT_HERSHEY_TRIPLEX,
            5,
            (0, 0, 0),
            2,
        )

        return Image.fromarray(img)

    def generate_puzzle(self):
        random.seed(self.metadata.seed)
        original_image = self.create_image()
        # Load the image
        original_width, original_height = original_image.size
        cols = 5
        rows = 2

        # Calculate dimensions for each puzzle piece
        piece_width = original_width // cols
        piece_height = original_height // rows

        # Create a list to hold shuffled puzzle pieces
        puzzle_pieces = []

        # Create puzzle pieces
        for y in range(0, original_height, piece_height):
            for x in range(0, original_width, piece_width):
                box = (x, y, x + piece_width, y + piece_height)
                puzzle_piece = original_image.crop(box)
                puzzle_pieces.append(puzzle_piece)

        # Shuffle the puzzle pieces
        random.shuffle(puzzle_pieces)

        # Create a new blank image to paste puzzle pieces onto
        puzzle_image = Image.new(
            "RGB", (original_width *
                    2, original_height *
                    2), (255, 255, 255)
        )
        # puzzle_image.

        # Paste shuffled puzzle pieces onto the blank image
        for i, piece in enumerate(puzzle_pieces):
            x = (i % cols) * piece_width * 2 + 25
            y = (i % rows) * piece_height * 2 + 25
            rotation_angle = random.randint(0, 360)
            piece = piece.rotate(rotation_angle, expand=True,
                                 fillcolor=(255, 255, 255))
            puzzle_image.paste(piece, (x, y))

        puzzle = pageTypes.Content(
            type=pageTypes.ContentType.IMAGE,
            content=puzzle_image)

        hint1 = pageTypes.Content(
            type=pageTypes.ContentType.TEXT,
            content="Solve the jigsaw puzzle for the code"
        )

        hint2 = pageTypes.Content(
            type=pageTypes.ContentType.TEXT,
            content=""
        )

        return pageTypes.PuzzleInfo(
            mainPuzzle=puzzle, hints=[hint1, hint2])

    @classmethod
    def get_metadata(cls):
        return SeedMetadata
