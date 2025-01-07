from abc import ABC, abstractmethod
from itertools import cycle
from pathlib import Path
import random
from fpdf import FPDF, FlexTemplate
from src.pages.pageTypes import ContentType
from src.pages.layouts import layout_map
from src.pages.pageTypes import PageType


current_dir = Path(__file__).parent


def render_puzzle(tmpl, puzzle):
    if puzzle.type == ContentType.IMAGE:
        tmpl["puzzle_image"] = puzzle.content
    else:
        tmpl["puzzle_text"] = puzzle.content


def render_hint(tmpl, hint, hint_no):
    if hint.type == ContentType.IMAGE:
        tmpl[f"hint_{hint_no}_image"] = hint.content
    else:
        tmpl[f"hint_{hint_no}_text"] = hint.content


class Page(ABC):
    def __init__(self, title, theme, layout, pageNumber, pageType):
        self.title = title
        self.theme = theme
        papers = theme.get_papers()
        graphics = theme.get_graphics()
        random.shuffle(papers)
        random.shuffle(graphics)
        self.papers = cycle(papers)
        self.graphics = cycle(graphics)
        self.layout = layout.copy()
        self.pageNumber = pageNumber
        self.pageType = pageType

    def createPage(self):
        pdf = FPDF()
        pdf.set_page_background(next(self.papers))
        pdf.add_page()
        pdf.set_auto_page_break(False)
        self.add_fonts(pdf)
        tmpl = FlexTemplate(pdf, elements=self.layout['elements'])
        tmpl["page_no"] = self.pageNumber
        tmpl["title"] = self.title

        if self.layout["has_paper"]:
            tmpl["paper"] = next(self.papers)

        for i in range(self.layout["graphic_count"]):
            tmpl[f"graphic_{i}"] = next(self.graphics)

        self.render_content(pdf, tmpl)
        tmpl.render()
        return pdf

    def add_fonts(self, pdf):
        (header_font, header_font_loc) = self.theme.get_header_font()
        (body_font, body_font_loc) = self.theme.get_body_font()

        for elem in self.layout['elements']:
            if elem['type'] == 'T':
                if elem['name'] == "header" or elem['name'] == "title":
                    elem['font'] = header_font
                else:
                    elem['font'] = body_font

        pdf.add_font(header_font, '', header_font_loc, uni=True)
        pdf.add_font(body_font, '', body_font_loc, uni=True)

        pdf.add_font(fname=f'{current_dir}/Waree.ttf')
        pdf.set_fallback_fonts(['Waree'])

    @abstractmethod
    def render_content(self, pdf, tmpl):
        pass


class FrontPageNoStory(Page):
    def __init__(
            self, title, theme, layout_index, pageNumber, puzzle, hint_1,
            hint_2, difficulty, reqs, header):
        super().__init__(title, theme,
                         layout_map[PageType.FRONT_NO_STORY][layout_index],
                         pageNumber, PageType.FRONT_NO_STORY)

        self.puzzle = puzzle
        self.hint_1 = hint_1
        self.hint_2 = hint_2
        self.difficulty = difficulty
        self.reqs = reqs
        self.header = header

    def render_content(self, pdf, tmpl):
        render_puzzle(tmpl, self.puzzle)
        render_hint(tmpl, self.hint_1, 1)
        render_hint(tmpl, self.hint_2, 2)

        reqs_string = f"""
-- Puzzle Info --
Difficulty: {self.difficulty}
Requirements:
    Pen
{
    "    " + chr(10) + "    ".join(self.reqs) if self.reqs else ""
}
"""
        tmpl["reqs"] = reqs_string
        tmpl["header"] = self.header


class FrontPageWithStory(Page):
    def __init__(
        self, title, theme, layout_index, pageNumber,
        puzzle, hint_1, hint_2, difficulty, reqs, intro, header, story
    ):
        super().__init__(
            title, theme, layout_map[PageType.FRONT_WITH_STORY][layout_index],
            pageNumber, PageType.FRONT_WITH_STORY)
        self.puzzle = puzzle
        self.hint_1 = hint_1
        self.hint_2 = hint_2
        self.difficulty = difficulty
        self.header = header
        self.intro = intro
        self.reqs = reqs
        self.story = story

    def render_content(self, pdf, tmpl):
        render_puzzle(tmpl, self.puzzle)
        render_hint(tmpl, self.hint_1, 1)
        render_hint(tmpl, self.hint_2, 2)

        reqs_string = f"""
-- Puzzle Info --
Difficulty: {self.difficulty}
Requirements:
    Pen
{
    "    " + chr(10) + "    ".join(self.reqs) if self.reqs else ""
}
"""
        tmpl["reqs"] = reqs_string
        tmpl["header"] = self.header
        tmpl["intro"] = self.intro
        tmpl["story"] = self.story


class PuzzlePageNoStory(Page):
    def __init__(self, title, theme, layout_index, pageNumber,
                 puzzle, hint_1, hint_2
                 ):
        super().__init__(
            title,
            theme,
            layout_map[PageType.PUZZLE_NO_STORY][layout_index],
            pageNumber, PageType.PUZZLE_NO_STORY)
        self.puzzle = puzzle
        self.hint_1 = hint_1
        self.hint_2 = hint_2

    def render_content(self, pdf, tmpl):
        render_puzzle(tmpl, self.puzzle)
        render_hint(tmpl, self.hint_1, 1)
        render_hint(tmpl, self.hint_2, 2)


class PuzzlePageWithStory(Page):
    def __init__(self, title, theme, layout_index, pageNumber,
                 puzzle, hint_1, hint_2, story
                 ):
        super().__init__(
            title,
            theme,
            layout_map[PageType.PUZZLE_WITH_STORY][layout_index],
            pageNumber, PageType.PUZZLE_WITH_STORY)
        self.puzzle = puzzle
        self.hint_1 = hint_1
        self.hint_2 = hint_2
        self.story = story

    def render_content(self, pdf, tmpl):
        render_puzzle(tmpl, self.puzzle)
        render_hint(tmpl, self.hint_1, 1)
        render_hint(tmpl, self.hint_2, 2)
        tmpl["story"] = self.story


class ConclusionPageWithStory(Page):
    def __init__(self, title, theme, layout_index, pageNumber, story):
        super().__init__(
            title,
            theme,
            layout_map[PageType.CONCLUSION][layout_index],
            pageNumber, PageType.CONCLUSION
        )
        self.story = story

    def render_content(self, pdf, tmpl):
        tmpl["story"] = self.story
