from src.puzzle.generator import Generator, NoneMetadata
import src.pages.pageTypes as pageTypes
import cv2
from PIL import Image
from pathlib import Path

cur_dir = Path(__file__).parent


class Mirror(Generator):

    def create_image(self):
        print(self.solution)
        img_list = []
        for c in self.solution:
            img = cv2.imread(
                f"{cur_dir}/mirror_numbers/{c}.png", cv2.IMREAD_UNCHANGED)
            img_list.append(img)

        combined_img = cv2.hconcat(img_list)
        return Image.fromarray(combined_img)

    def generate_puzzle(self):
        puzzle_image = self.create_image()

        puzzle = pageTypes.Content(
            type=pageTypes.ContentType.IMAGE,
            content=puzzle_image
        )

        hint1 = pageTypes.Content(
            type=pageTypes.ContentType.TEXT,
            content="",
        )

        hint2 = pageTypes.Content(
            type=pageTypes.ContentType.TEXT,
            content="")

        return pageTypes.PuzzleInfo(
            mainPuzzle=puzzle,
            hints=[hint1, hint2]
        )

    @classmethod
    def get_metadata(cls):
        return NoneMetadata
