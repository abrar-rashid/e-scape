import random

import cv2
import numpy as np
import src.pages.pageTypes as pageTypes
from PIL import Image
from src.puzzle.generator import Generator, SeedMetadata


class Steganograph(Generator):

    def create_image(self):
        # Create a blank canvas
        canvas = np.zeros((300, 500), dtype=np.uint8)
        gaussian_noise = np.zeros((300, 500), dtype=np.uint8)
        cv2.randn(gaussian_noise, 0, 500)
        canvas = cv2.add(canvas, gaussian_noise)

        # Draw the solution on the canvas
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 2
        font_thickness = 1
        text_size = cv2.getTextSize(self.solution,
                                    font,
                                    font_scale,
                                    font_thickness)[0]
        text_x = int((canvas.shape[1] - text_size[0]) / 2.3)
        text_y = int((canvas.shape[0] + text_size[1]) / 2.3)
        cv2.putText(canvas, self.solution, (text_x, text_y), font,
                    font_scale,
                    (255, 255, 255), font_thickness)

        return Image.fromarray(canvas)

    def generate_puzzle(self):
        img_path = self.create_image()
        random.seed(self.metadata.seed)

        puzzle = pageTypes.Content(
            type=pageTypes.ContentType.IMAGE,
            content=img_path
        )

        hint1 = pageTypes.Content(
            type=pageTypes.ContentType.TEXT,
            content="",
        )

        hint2 = pageTypes.Content(
            type=pageTypes.ContentType.TEXT,
            content="Focus and the truth shall be clear"
        )

        return pageTypes.PuzzleInfo(
            mainPuzzle=puzzle,
            hints=[hint1, hint2]
        )

    @classmethod
    def get_metadata(cls):
        return SeedMetadata
