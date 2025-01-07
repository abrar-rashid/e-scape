from pathlib import Path

import src.pages.pageTypes as pageTypes
from PIL import Image, ImageDraw, ImageFont
from src.puzzle.generator import Generator, NoneMetadata


class CutAndFold(Generator):

    width = 400
    height = 400
    digit_font_size = 60
    cur_dir = Path(__file__).parent
    digit_font = ImageFont.truetype(
        f"{cur_dir}/font.ttf", digit_font_size
    )
    letter_font_size = 20
    letter_font = ImageFont.truetype(
        f"{cur_dir}/font.ttf", letter_font_size
    )

    def get_rotated_image(self, x, ang):
        rotated_img = Image.new("RGB",
                                (self.digit_font_size, self.digit_font_size),
                                "white")
        draw_rotated_digit = ImageDraw.Draw(rotated_img)
        draw_rotated_digit.text((0, 0), x, fill="black", font=self.digit_font)
        rotated_img = rotated_img.rotate(ang)
        return rotated_img

    def get_letter_image(self, c):
        letter_img = Image.new("RGB",
                               (self.letter_font_size, self.letter_font_size),
                               "white")
        draw_letter = ImageDraw.Draw(letter_img)
        draw_letter.text((0, 0), c, fill="black", font=self.letter_font)
        return letter_img

    def draw_first_digit(self, x, img):
        img.paste(self.get_rotated_image(x, 0),
                  (self.width // 4,
                   self.height - self.digit_font_size // 2))

        img.paste(self.get_letter_image("A"),
                  (self.width // 4 + self.letter_font_size,
                  self.height - self.digit_font_size // 2 - 10))

        img.paste(self.get_rotated_image(x, 180),
                  ((self.width * 3) // 4 - self.digit_font_size // 2,
                  self.height - self.digit_font_size // 2))

        img.paste(self.get_letter_image("A"),
                  ((self.width * 3) // 4 - self.digit_font_size // 2
                   + self.letter_font_size,
                  self.height - self.digit_font_size // 2 - 10))

    def draw_second_digit(self, x, img):
        img.paste(self.get_rotated_image(x, 90),
                  (self.width - self.digit_font_size // 2,
                  (self.height * 3) // 4 - self.digit_font_size // 2))

        img.paste(self.get_letter_image("B"),
                  (self.width - self.digit_font_size // 2
                   - self.letter_font_size,
                  (self.height * 3) // 4 - self.digit_font_size // 2))

        img.paste(self.get_rotated_image(x, 270),
                  (self.width - self.digit_font_size // 2,
                  self.height // 4 - self.digit_font_size // 2))

        img.paste(self.get_letter_image("B"),
                  (self.width - self.digit_font_size // 2
                   - self.letter_font_size,
                  self.height // 4 - self.digit_font_size // 2))

    def draw_third_digit(self, x, img):
        img.paste(self.get_rotated_image(x, 180),
                  ((self.width * 3) // 4 - self.digit_font_size // 2,
                  -self.digit_font_size // 2))

        img.paste(self.get_letter_image("C"),
                  ((self.width * 3) // 4,
                  self.digit_font_size // 2))

        img.paste(self.get_rotated_image(x, 0),
                  (self.width // 4 - self.digit_font_size // 2,
                  -self.digit_font_size // 2))

        img.paste(self.get_letter_image("C"),
                  (self.width // 4 - self.digit_font_size // 2,
                  self.digit_font_size // 2))

    def draw_fourth_digit(self, x, img):
        img.paste(self.get_rotated_image(x, 270),
                  (- self.digit_font_size // 2,
                  self.height // 4 - self.digit_font_size // 2))

        img.paste(self.get_letter_image("D"),
                  (self.width // 4 - self.digit_font_size,
                  self.height // 4 - self.digit_font_size // 2))

        img.paste(self.get_rotated_image(x, 90),
                  (- self.digit_font_size // 2,
                  (self.height * 3) // 4 - self.digit_font_size // 2))

        img.paste(self.get_letter_image("D"),
                  (self.width // 4 - self.digit_font_size,
                  (self.height * 3) // 4))

    def draw_fifth_digit(self, x, img):
        img.paste(self.get_rotated_image(x, 90),
                  (self.width - self.digit_font_size // 2,
                  -(self.digit_font_size * 3) // 4))

        img.paste(self.get_letter_image("E"),
                  (self.width - self.letter_font_size,
                  self.letter_font_size))

        img.paste(self.get_rotated_image(x, 270),
                  (-self.digit_font_size // 2,
                  -self.digit_font_size // 4))

        img.paste(self.get_letter_image("E"),
                  (self.letter_font_size,
                  self.letter_font_size))

        img.paste(self.get_rotated_image(x, 90),
                  (-self.digit_font_size // 2,
                  self.height - (self.digit_font_size * 3) // 4))

        img.paste(self.get_letter_image("E"),
                  (self.letter_font_size,
                  self.height - self.letter_font_size))

        img.paste(self.get_rotated_image(x, 270),
                  (self.width - self.digit_font_size // 2,
                  self.height - self.digit_font_size // 4))

        img.paste(self.get_letter_image("E"),
                  (self.width - self.letter_font_size,
                  self.height - 2 * self.letter_font_size))

    def draw_sixth_digit(self, x, img):
        img.paste(self.get_rotated_image(x, 0),
                  (self.width - self.digit_font_size // 4,
                  self.height // 2 - self.digit_font_size // 2))

        img.paste(self.get_letter_image("F"),
                  (self.width - self.digit_font_size // 2,
                  self.height // 2 - self.digit_font_size // 2))

        img.paste(self.get_rotated_image(x, 180),
                  (self.width // 2 - self.digit_font_size // 2,
                  -self.digit_font_size // 2))

        img.paste(self.get_letter_image("F"),
                  (self.width // 2,
                  self.letter_font_size))

        img.paste(self.get_rotated_image(x, 0),
                  (-self.digit_font_size // 4,
                  self.height // 2 - self.digit_font_size // 2))

        img.paste(self.get_letter_image("F"),
                  (2 * self.letter_font_size,
                  self.height // 2 - self.digit_font_size // 2))

        img.paste(self.get_rotated_image(x, 180),
                  (self.width // 2 - self.digit_font_size // 2,
                  self.height - self.digit_font_size // 2))

        img.paste(self.get_letter_image("F"),
                  (self.width // 2,
                  self.height - 2 * self.letter_font_size))

    def create_image(self, digits):
        img = Image.new("RGB", (self.width, self.height), "white")

        self.draw_first_digit(digits[0], img)
        self.draw_second_digit(digits[1], img)
        self.draw_third_digit(digits[2], img)
        self.draw_fourth_digit(digits[3], img)
        self.draw_fifth_digit(digits[4], img)
        self.draw_sixth_digit(digits[5], img)

        return img

    def generate_puzzle(self):
        image = self.create_image(str(self.solution))
        puzzle = pageTypes.Content(
            type=pageTypes.ContentType.IMAGE,
            content=image
        )

        hint1 = pageTypes.Content(
            type=pageTypes.ContentType.TEXT,
            content="Cut and fold to reveal a code.")

        hint2 = pageTypes.Content(
            type=pageTypes.ContentType.TEXT,
            content="",
        )

        return pageTypes.PuzzleInfo(
            mainPuzzle=puzzle,
            hints=[hint1, hint2]
        )

    @classmethod
    def get_metadata(cls):
        return NoneMetadata
