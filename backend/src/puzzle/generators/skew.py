from src.puzzle.generator import Generator, NoneMetadata
import src.pages.pageTypes as pageTypes
import cv2
import numpy as np
from PIL import Image


class Skew(Generator):

    def create_image(self):
        # no return since it'll eventually be stored in a database?
        img = np.zeros((150, 675, 4), dtype=np.uint8)
        cv2.putText(img, str(self.solution), (35, 130),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    5, (0, 0, 0, 255), 12, cv2.LINE_AA)

        return Image.fromarray(img)

    def generate_puzzle(self):
        original_image = self.create_image()
        original_width, original_height = original_image.size

        puzzle_image = original_image.resize(
            (int(original_width / 1.3), original_height * 20))
        puzzle = pageTypes.Content(
            type=pageTypes.ContentType.IMAGE,
            content=puzzle_image
        )

        hint1 = pageTypes.Content(
            type=pageTypes.ContentType.TEXT,
            content=""
        )

        hint2 = pageTypes.Content(
            type=pageTypes.ContentType.TEXT,
            content="Sometimes all you need is a new perspective"
        )

        return pageTypes.PuzzleInfo(
            mainPuzzle=puzzle,
            hints=[hint1, hint2]
        )

    @classmethod
    def get_metadata(cls):
        return NoneMetadata
