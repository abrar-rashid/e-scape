from reportlab.lib.pagesizes import A4
from src.pages.flowable import FixedFlowable, RotatingParagraph


def create_answers(answers):
    answer_list = []
    for i, answer in enumerate(answers):
        answer_list.append(f"{i+1}. {answer}\n")

    width, height = A4
    return FixedFlowable(
        RotatingParagraph(
            "<br/>" +
            "<br/><br/>".join(answer_list), 0, width * 0.8, height * 0.7
        )
    )
