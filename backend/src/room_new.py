from concurrent.futures import ThreadPoolExecutor
import io
import itertools
import random
from itertools import cycle
from os import chdir
from pathlib import Path
from src.storyline import Storyline
from src.pages.page_new import ConclusionPageWithStory, FrontPageNoStory, \
    FrontPageWithStory, PuzzlePageNoStory, PuzzlePageWithStory
from src.pages.pageTypes import (
    Difficulty,
    Theme,
    PuzzleType,
)
from pypdf import PdfMerger


def _create_page(p):
    return io.BytesIO(p.createPage().output())


class Room:

    def __init__(
        self,
        theme,
        keywords,
        difficulty,
        length,
        whitelist,
        blacklist,
        include_storyline=True,
        is_public=False
    ) -> None:
        if not isinstance(theme, Theme):
            raise TypeError("theme must be of type Theme")
        self.is_public = is_public
        self.theme: Theme = theme
        self.keywords: list[str] = keywords
        if not isinstance(difficulty, Difficulty):
            raise TypeError("difficulty must be of type Difficulty")
        self.difficulty: Difficulty = difficulty
        self.length: int = length
        self.whitelist: list[PuzzleType] = whitelist
        self.blacklist: list[PuzzleType] = blacklist
        self.include_storyline = include_storyline
        self.puzzles: list[PuzzleType] = []
        # self.seed = random.randint(0, 10000)

        # Whitelisted puzzles are valid, added to puzzle_types
        puzzle_types = self.whitelist.copy()

        # Gets all puzzle types
        puzzle_candidates = PuzzleType.as_set()
        puzzle_candidates -= set(self.whitelist)
        puzzle_candidates -= set(self.blacklist)

        # Puzzles of difficulty <= desired difficulty are valid
        # so will be added to puzzle types
        puzzle_candidates = list(
            filter(
                lambda p: PuzzleType.get_difficulty(
                    PuzzleType(p)) <= self.difficulty,
                puzzle_candidates,
            )
        )
        puzzle_candidates = list(puzzle_candidates)
        random.shuffle(puzzle_candidates)
        puzzle_candidates = set(puzzle_candidates)
        puzzle_candidates = sorted(
            puzzle_candidates,
            key=lambda p: PuzzleType.get_difficulty(PuzzleType(p)),
            reverse=True,
        )
        puzzle_types.extend(puzzle_candidates)

        # Cycles through the puzzle types in case there are not enough
        # puzzles
        self.puzzles = list(
            itertools.islice(
                cycle(puzzle_types),
                self.length))

        self.generators = list(
            map(lambda p: PuzzleType(
                p).get_generator().get_random(), self.puzzles)
        )

        if self.include_storyline:
            self.generate_storyline()
        else:
            self.storyline = Storyline(self.theme, self.keywords,
                                       self.difficulty,
                                       self.length, self.puzzles)

    def create_room(self):

        chdir(Path(__file__).parent)

        intro_page = None

        puzzle_1 = self.generators[0].generate_puzzle()

        if self.include_storyline:
            intro_page = FrontPageWithStory(
                "Phase 1",
                self.theme,
                0,
                '1',
                puzzle_1.mainPuzzle,
                puzzle_1.hints[0],
                puzzle_1.hints[1],
                self.difficulty,
                "",
                self.storyline.introduction,
                f"{str(self.theme)} Escape Room",
                self.get_story_by_phase(1)
            )
        else:
            intro_page = FrontPageNoStory(
                "Phase 1",
                self.theme,
                0,
                '1',
                puzzle_1.mainPuzzle,
                puzzle_1.hints[0],
                puzzle_1.hints[1],
                self.difficulty,
                "",
                f"{str(self.theme)} Escape Room",
            )

        pages = [intro_page]
        for i, gen in enumerate(self.generators[1:]):
            puzzle = gen.generate_puzzle()
            page = None
            if self.include_storyline:
                page = PuzzlePageWithStory(
                    f"Phase {i+2}",
                    self.theme,
                    0,
                    f'{i+2}',
                    puzzle.mainPuzzle,
                    puzzle.hints[0],
                    puzzle.hints[1],
                    self.get_story_by_phase(i + 2),
                )
            else:
                page = PuzzlePageNoStory(
                    f"Phase {i+2}",
                    self.theme,
                    0,
                    f'{i+2}',
                    puzzle.mainPuzzle,
                    puzzle.hints[0],
                    puzzle.hints[1],
                )

            pages.append(page)

        if self.include_storyline:
            conclusion_page = ConclusionPageWithStory(
                "Conclusion",
                self.theme,
                0,
                f'{self.length + 1}',
                self.storyline.conclusion,
            )
            pages.append(conclusion_page)

        merger = PdfMerger()
        pdf_pages = None
        # with Pool() as P:
        #     pdf_pages = P.map(
        #         lambda p: io.BytesIO(p.createPage().output()), pages
        #         )
        # pdf_pages = map(
        #         lambda p: io.BytesIO(p.createPage().output()), pages
        #         )
        with ThreadPoolExecutor() as executor:
            pdf_pages = executor.map(lambda p: io.BytesIO(p.createPage().output()), pages)

        for page in pdf_pages:
            merger.append(page)
        output = io.BytesIO()
        merger.write(output)
        merger.close()
        output.seek(0)
        return output

    # def get_path(self):
    #     return self.path

    def regen_room(self):

        old_generators = self.generators
        self.generators = list(map(
            lambda p: PuzzleType(p).get_generator().get_random(), self.puzzles)
        )
        [self.set_solution(i + 1, old_generators[i].solution) for i in range
         (len(old_generators))]
        return self.create_room()

    def generate_storyline(self):
        # Generates a Storyline type
        self.storyline = Storyline(self.theme, self.keywords,
                                   self.difficulty,
                                   self.length, self.puzzles)
        self.storyline.generate_introduction()
        self.storyline.generate_phases()
        self.storyline.generate_conclusion()
        self.storyline.generate_failure()

    def get_puzzle(self, index):
        return self.puzzles[index - 1]

    def get_puzzles(self):
        return self.puzzles

    def get_solutions(self):
        return [s.solution for s in self.generators]

    def set_solutions(self, new_solutions):
        for generator, new_solution in zip(self.generators, new_solutions):
            generator.solution = new_solution

    def set_solution(self, index, new_solution):
        self.generators[index - 1].solution = new_solution

    def get_intro(self):
        return self.storyline.introduction

    def get_story_by_phase(self, index):
        return self.storyline.phases[index - 1]

    def get_story_phases(self):
        return self.storyline.phases

    def get_conclusion(self):
        return self.storyline.conclusion

    def get_failure(self):
        return self.storyline.failure

    def set_puzzle(self, index, puzzleType):
        self.puzzles[index - 1] = puzzleType

    def regen_intro(self):
        self.storyline.generate_introduction()

    def regen_story_by_phase(self, index):
        self.storyline.regenerate_puzzle_phase(
            index, PuzzleType(self.get_puzzle(index)).get_name())

    def regen_story_phases(self):
        self.storyline.generate_phases()

    def regen_conclusion(self):
        self.storyline.generate_conclusion()

    def regen_failure(self):
        self.storyline.generate_failure()

    def set_intro_man(self, introduction):
        self.storyline.introduction = introduction

    def set_story_by_phase_man(self, index, content):
        self.storyline.phases[index - 1] = content

    def set_story_phases(self, contentList):
        self.storyline.phases = contentList

    def set_conclusion_man(self, conclusion):
        self.storyline.conclusion = conclusion

    def set_failure_man(self, failure):
        self.storyline.failure = failure

    def set_public(self, value):
        self.is_public = value
