import random
from collections import deque
import io
from src.puzzle.generator import Generator, SeedMetadata
from src.pages import pageTypes
import cairosvg


class Cell:
    # Walls for cell pairs - the north wall of one cell
    # is the south wall of its north neighbour
    divisions = {"N": "S", "S": "N", "E": "W", "W": "E"}

    def __init__(self, x, y):
        # A cell initially has all walls present.
        self.x, self.y = x, y
        self.walls = {"N": 1, "S": 1, "E": 1, "W": 1}

    def all_walls_present(self):
        return all(self.walls.values())

    def remove_wall(self, other, wall):
        self.walls[wall] = 0
        if other:
            other.walls[Cell.divisions[wall]] = 0


class Maze(Generator):
    # A 2d array of cells
    def __init__(self, solution, metadata: SeedMetadata, rows=30, cols=30):
        # Change rows and cols to make easier or harder
        self.rows, self.cols = rows, cols
        self.grid = [[Cell(x, y) for y in range(rows)]
                     for x in range(cols)]
        self.solution_path: list[tuple[int, int]] = []
        super().__init__(solution, metadata)

    def generate_puzzle(self):
        random.seed(self.metadata.seed)
        self.create_maze()
        solution_path = self.solve_maze()
        svg_string = ""
        print("Solving maze...\n")
        try:
            svg_string = self.create_svg(solution_path)
            print("Solution path:", solution_path)
            print("\nPuzzle solution:", self.solution)
        except Exception:
            # Should never happen
            print("Error, no solution found.")

        img_bytesio = io.BytesIO()
        cairosvg.svg2png(bytestring=svg_string, write_to=img_bytesio)

        puzzle = pageTypes.Content(
            type=pageTypes.ContentType.IMAGE,
            content=img_bytesio
        )

        hint1 = pageTypes.Content(
            type=pageTypes.ContentType.TEXT,
            content="Revalation awaits through navigation"
        )

        hint2 = pageTypes.Content(
            type=pageTypes.ContentType.TEXT,
            content="",
        )

        return pageTypes.PuzzleInfo(
            mainPuzzle=puzzle, hints=[hint1, hint2])

    def find_legal_neighbours(self, cell):
        # Finds all unvisited neighbours
        step = [("W", (-1, 0)), ("E", (1, 0)),
                ("S", (0, 1)), ("N", (0, -1))]
        neighbours = []
        for direction, (dx, dy) in step:
            x2, y2 = cell.x + dx, cell.y + dy
            if (0 <= x2 < self.cols) and (0 <= y2 < self.rows):
                neighbour = self.grid[x2][y2]
                if neighbour.all_walls_present():
                    neighbours.append((direction, neighbour))
        return neighbours

    def create_maze(self):
        # Total number of cells.
        total = self.cols * self.rows
        cell_stack = []
        current_cell = self.grid[0][0]
        # Total number of visited cells during maze construction.
        index = 1

        while index < total:
            neighbours = self.find_legal_neighbours(current_cell)

            if not neighbours:
                # We've reached a dead end: backtrack.
                current_cell = cell_stack.pop()
                continue

            # Choose a random neighbouring cell and move to it.
            direction, next_cell = random.choice(neighbours)
            current_cell.remove_wall(next_cell, direction)
            cell_stack.append(current_cell)
            current_cell = next_cell
            index += 1

    def solve_maze(self):
        # Solving the maze using breadth-first search.
        start_cell = self.grid[0][0]
        end_cell = self.grid[self.cols - 1][self.rows - 1]
        visited = set()
        queue = deque([(start_cell, [])])

        while queue:
            current_cell, path = queue.popleft()
            if current_cell in visited:
                continue
            visited.add(current_cell)
            if current_cell == end_cell:
                return path + [(current_cell.x, current_cell.y)]

            for direction in current_cell.walls:
                if not current_cell.walls[direction]:
                    x2, y2 = current_cell.x, current_cell.y
                    if direction == "N":
                        y2 -= 1
                    elif direction == "S":
                        y2 += 1
                    elif direction == "E":
                        x2 += 1
                    elif direction == "W":
                        x2 -= 1

                    next_cell = self.grid[x2][y2]

                    if next_cell not in visited:
                        new_path = path + \
                            [(current_cell.x, current_cell.y)]
                        queue.append((next_cell, new_path))
        return None

    def create_svg(self, solution_path):
        aspect_ratio = self.cols / self.rows
        padding = 10
        height = 500
        width = int(height * aspect_ratio)
        scy, scx = height / self.rows, width / self.cols

        string_buffer = io.StringIO()

        """ Randomly select 6 positions from the solution path
        but must maintain order of path for the solution
        positions. This is so that the 6 digit puzzle solution
        is ordered by the solution path."""
        solution_path_ordered = enumerate(solution_path)
        ordered_positions = sorted(
            random.sample(list(solution_path_ordered), 6))
        solution_positions = [j for _, j in ordered_positions]
        # Randomly select additional positions on the grid
        grid_positions = [
            (x, y)
            for x in range(self.cols)
            for y in range(self.rows)
            if (x, y) not in solution_path
        ]

        # Select 6 additional positions from the grid positions
        grid_positions = random.sample(grid_positions, 24)

        # Combine solution and grid positions
        num_positions = solution_positions + grid_positions

        # Remove the wall 'N' of the first cell
        self.grid[0][0].remove_wall(self.grid[0][0], "N")

        # Remove down the wall 'S' of the last cell
        self.grid[self.cols - 1][self.rows - 1].remove_wall(
            self.grid[self.cols - 1][self.rows - 1], "S"
        )

        print('<?xml version="1.0" encoding="utf-8"?>', file=string_buffer)
        print('<svg xmlns="http://www.w3.org/2000/svg"', file=string_buffer)
        print(
            '    width="{:d}" height="{:d}" viewBox="{} {} {} {}">'.format(
                width + 2 * padding,
                height + 2 * padding,
                -padding,
                -padding,
                width + 2 * padding,
                height + 2 * padding,
            ),
            file=string_buffer,
        )
        print('<defs>\n<style type="text/css"><![CDATA[', file=string_buffer)
        print("line {", file=string_buffer)
        print(
            "    stroke: #000000;\n    stroke-linecap: square;",
            file=string_buffer)
        print("    stroke-width: 3;\n}", file=string_buffer)
        print("text {", file=string_buffer)
        print("    font-size: 12px;\n    text-anchor: middle;",
              file=string_buffer)
        # Can change colour if needed
        print("    fill: black;", file=string_buffer)
        print("}", file=string_buffer)
        print("]]></style>\n</defs>", file=string_buffer)

        # Draw the maze walls
        for x in range(self.cols):
            for y in range(self.rows):
                cell = self.grid[x][y]
                if cell.walls["N"]:
                    x1, y1, x2, y2 = x * scx, y * \
                        scy, (x + 1) * scx, y * scy
                    print(
                        '<line x1="{}" y1="{}" x2="{}" y2="{}"/>'.format(
                            x1, y1, x2, y2
                        ),
                        file=string_buffer,
                    )
                if cell.walls["W"]:
                    x1, y1, x2, y2 = x * scx, y * \
                        scy, x * scx, (y + 1) * scy
                    print(
                        '<line x1="{}" y1="{}" x2="{}" y2="{}"/>'.format(
                            x1, y1, x2, y2
                        ),
                        file=string_buffer,
                    )
                if cell.walls["S"]:
                    x1, y1, x2, y2 = (
                        x * scx,
                        (y + 1) * scy,
                        (x + 1) * scx,
                        (y + 1) * scy,
                    )
                    print(
                        '<line x1="{}" y1="{}" x2="{}" y2="{}"/>'.format(
                            x1, y1, x2, y2
                        ),
                        file=string_buffer,
                    )
                if cell.walls["E"]:
                    x1, y1, x2, y2 = (
                        (x + 1) * scx,
                        y * scy,
                        (x + 1) * scx,
                        (y + 1) * scy,
                    )
                    print(
                        '<line x1="{}" y1="{}" x2="{}" y2="{}"/>'.format(
                            x1, y1, x2, y2
                        ),
                        file=string_buffer,
                    )

        digits = [int(d) for d in str(self.solution)]
        i = 0
        for x, y in num_positions:
            digit = str(random.randint(0, 9))
            if (x, y) in solution_path:
                digit = digits[i]
                i += 1
            print(
                '<text x="{}" y="{}">{}</text>'.format(
                    (x + 0.5) * scx, (y + 0.75) * scy, digit
                ),
                file=string_buffer,
            )
        print("</svg>", file=string_buffer)

        svg_string = string_buffer.getvalue()
        return svg_string

    @classmethod
    def get_metadata(cls):
        return SeedMetadata
