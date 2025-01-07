import io
from src.puzzle.generator import Generator, NoneMetadata
from svgwrite import Drawing
from src.pages import pageTypes
import cairosvg


class ConnectDots(Generator):

    def generate_puzzle(self):
        puzzle_image = self.connect_the_dots()

        puzzle = pageTypes.Content(
            type=pageTypes.ContentType.IMAGE,
            content=puzzle_image,
        )

        hint1 = pageTypes.Content(
            type=pageTypes.ContentType.TEXT,
            content="",)

        hint2 = pageTypes.Content(
            type=pageTypes.ContentType.TEXT,
            content="Once the constellations align, truth shall be observed.")

        return pageTypes.PuzzleInfo(mainPuzzle=puzzle, hints=[hint1, hint2])

    def connect_the_dots(self):
        number = str(self.solution)
        margin = 10
        dwg = Drawing(
            filename="connectdots.svg", size=(f"{650}px", f"{750}px"))
        dot_coords = {
            "0": [(46, 269), (19, 270), (19, 187), (16, 67),
                  (42, 64), (66, 67), (63, 143), (65, 265)],
            "1": [(20, 45), (40, 20), (38, 71), (43, 165),
                  (45, 198), (44, 267), (24, 267), (64, 267)],
            "2": [(10, 90), (36, 52), (64, 76), (50, 130),
                  (32, 180), (10, 249), (42, 236), (64, 249)],
            "3": [(10, 245), (38, 227), (60, 199), (61, 131),
                  (26, 149), (68, 105), (52, 33), (14, 56)],
            "4": [(30, 15), (11, 136), (28, 136), (63, 135),
                  (50, 85), (36, 191), (38, 257)],
            "5": [(67, 26), (30, 25), (27, 51), (26, 112),
                  (63, 75), (63, 125), (57, 189), (50, 250), (21, 243)],
            "6": [(58, 38), (31, 38), (25, 122), (24, 260),
                  (57, 260), (60, 150), (24, 134)],
            "7": [(19, 49), (47, 45), (71, 34), (43, 161),
                  (19, 163), (71, 159), (44, 138), (41, 243), (27, 300)],
            "8": [(64, 76), (32, 44), (10, 93), (35, 137),
                  (66, 214), (43, 264), (10, 193), (67, 93)],
            "9": [(21, 268), (64, 264), (61, 35), (14, 35),
                  (19, 129), (57, 125)]
        }
        dot_color = "black"
        line_color = "red"
        counter = 1
        g = dwg.g(stroke=line_color)

        prev_x, prev_y = dot_coords[number[0]][0]
        # Loop through each digit in the number
        for i, digit in enumerate(number):
            # Calculate the offset of the digit's box from the top-left corner
            offset_x = margin + i * (80 + margin)
            offset_y = margin + i * (80 + margin)
            # Loop through the coordinates of the dots for the digit
            for x, y in dot_coords[digit]:
                # Add the offset to the coordinates
                x += offset_x
                y += offset_y

                # Draw a circle for the dot
                dwg.add(dwg.circle(
                    center=(f"{x}px", f"{y}px"), r="2px", fill=dot_color))

                # Draw a text for the label
                dwg.add(dwg.text(
                    str(counter), insert=(f"{x+4}px", f"{y-5}px"),
                    fill=dot_color, font_size="15px"))

                # Add lines to the group
                g.add(dwg.line(
                    start=(prev_x, prev_y), end=(x, y), stroke_width=2))

                counter += 1
                prev_x, prev_y = x, y

        string_buffer = io.StringIO()

        dwg.write(string_buffer)

        svg_string = string_buffer.getvalue()

        img = io.BytesIO()
        cairosvg.svg2png(bytestring=svg_string, write_to=img)

        return img

    @classmethod
    def get_metadata(cls):
        return NoneMetadata
