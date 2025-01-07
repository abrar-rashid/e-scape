# from os import chdir
# from pathlib import Path
# from src.pages.pageTypes import (AspectRatio, Content, ContentType,
#                                  PageMetadata)
# from src.pages.page import createPage
# from dotenv import load_dotenv
# from src.storyline import generate_storyline
# from src.pages.pageTypes import Theme, PuzzleType
# from src.pages.flowable import RotatingParagraph, FixedFlowable
# from reportlab.lib.pagesizes import A4
# from src.puzzle.puzzle_new import create_puzzle
# from reportlab.pdfgen.canvas import Canvas
# from random import randint

# load_dotenv()


# def create_room(theme, keywords, difficulty, length):

#     # Generates the storyline as a list
#     story = generate_storyline(Theme.PIRATE, keywords, length)

#     # Need to change our current directory to this file's parent directory
#     # - Has to be in the top level python file that we run (this one)
#     chdir(Path(__file__).parent)

#     # create intro
#     width, height = A4
#     introduction = FixedFlowable(RotatingParagraph(story.introduction, 0,
#                                                    width*0.8,
#                                                    height * 0.7))
#     # All pages on one canvas to make everything on 1 pdf
#     canvas = Canvas(f"../../frontend/public/{theme.name}-Escape-Room.pdf",
#                     pagesize=A4)
#     createPage(theme, PageMetadata(
#         f"{theme.name} Introduction",
#         1,
#         Content(ContentType.FLOWABLE, introduction,
#                 AspectRatio.DEFAULT),
#         Content(ContentType.TEXT, "", AspectRatio.DEFAULT),
#         Content(ContentType.TEXT, "", AspectRatio.DEFAULT)),
#         canvas
#     )

#     solutions = []
# #     puzzle_types = []

#     # for loop to create puzzle story page and actual puzzle page
#     for i in range(1, length + 1):
#         content = story.phases[i - 1]
#         paragraph = FixedFlowable(
#             RotatingParagraph(content, 0, width*0.8, height * 0.65))
#         createPage(theme, PageMetadata(f"Phase {i}", i*2, Content(
#             ContentType.FLOWABLE, paragraph, AspectRatio.DEFAULT),
#             Content(ContentType.TEXT, "", AspectRatio.DEFAULT),
#             Content(ContentType.TEXT, "", AspectRatio.DEFAULT)), canvas)

#         # can now choose random puzzle and use the same code!
#         solution = randint(100000, 999999)
#         solutions.append(solution)
#         # puzzle_type = choice(PuzzleType)
#         # puzzle_types.append(puzzle_type)
#         puzzle = create_puzzle(
#             Theme.PIRATE, difficulty, PuzzleType.MORSE_CODE, solution
#         )
#         puzzle_flow = puzzle.mainPuzzle.content
#         hint1 = puzzle.hints[0].content
#         hint2 = puzzle.hints[1].content
#         createPage(theme,
#                    PageMetadata(f"Phase {i}", i*2 + 1,
#                                 Content(ContentType.FLOWABLE, puzzle_flow,
#                                         AspectRatio.DEFAULT),
#                                 Content(ContentType.FLOWABLE, hint1,
#                                         AspectRatio.DEFAULT),
#                                 Content(ContentType.FLOWABLE, hint2,
#                                         AspectRatio.DEFAULT)), canvas)

#     # create conclusion
#     c = story.conclusion
#     conclusion = FixedFlowable(RotatingParagraph(c, 0, width*0.8,
#     height*0.65))
#     createPage(theme, PageMetadata(
#         "Conclusion",
#         length * 2 + 2,
#         Content(ContentType.FLOWABLE, conclusion, AspectRatio.DEFAULT),
#         Content(ContentType.TEXT, "", AspectRatio.DEFAULT),
#         Content(ContentType.TEXT, "", AspectRatio.DEFAULT)), canvas
#     )
#     canvas.save()

#     return f"{theme.name}-Escape-Room.pdf"

#     # sanitise inputs

#     # set number pages and puzzles based on difficulty

#     # generate a storyline which is: list[story | puzzle(type, args)]
#     # create list of puzzles from the storyline: list[puzzle]
#     # puzzle: {content: Flowable, hints: list[Flowable]}

#     # we want to map from page num to main content: dict[int, Flowable]
#     # randomise hint placement over page range
#     # create map from pagenhints: dict[int, list[Flowable]]
#     # note that hints per page are capped at 2

#     # create templates(theme) for each page
#     # use map(s) to populate
#     # aggregate into a pdf
#     # pdf needs to store somewhere temporarily/permanently? tmp/
#     # other folder?
#     # return pdf

# # create_room(Theme.PIRATE, [""], di)
