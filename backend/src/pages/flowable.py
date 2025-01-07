from reportlab.graphics import renderPDF
from reportlab.platypus import Frame, Paragraph
from reportlab.platypus.flowables import Flowable
from svglib.svglib import svg2rlg


class RotatingParagraph(Flowable):
    """Rotates a text in a table cell."""

    def __init__(self, text, angle, width, height):
        Flowable.__init__(self)
        self.style = None
        self.text = text
        self.angle = angle
        self.frame = Frame(0, 0, width, height, showBoundary=0)

    def draw(self):
        canvas = self.canv
        # canvas.setFont(self.style.fontName, self.style.fontSize)
        canvas.rotate(self.angle)
        self.paragraph = [Paragraph(self.text, self.style)]
        self.frame.addFromList(self.paragraph, canvas)

    def setStyle(self, style):
        self.style = style


class RotatingImage(Flowable):

    def __init__(self, imagePath, angle, x, y, width, height):
        Flowable.__init__(self)
        self.image = imagePath
        self.angle = angle
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.frame = Frame(0, 0, width, height, showBoundary=0)

    def draw(self):
        canvas = self.canv
        canvas.rotate(self.angle)
        if self.image.endswith(".svg"):
            drawing = svg2rlg(self.image)
            renderPDF.draw(
                self.scale(
                    drawing,
                    0.85),
                canvas,
                self.x,
                self.y)
        else:
            canvas.drawImage(self.image, self.x, self.y,
                             self.width, self.height, mask='auto')
        # alt:
        # self.story = [self.scale(drawing, 0.5)]
        # self.frame.addFromList(self.story, canvas)
        # alt:
        # canvas.drawImage(self.image, self.x, self.y, self.width, self.height)

    def scale(self, drawing, scaling_factor):
        """
        Scale a reportlab.graphics.shapes.Drawing()
        object while maintaining the aspect ratio
        """
        scaling_x = scaling_factor
        scaling_y = scaling_factor

        drawing.width = drawing.minWidth() * scaling_x
        drawing.height = drawing.height * scaling_y
        drawing.scale(scaling_x, scaling_y)
        return drawing


class FixedFlowable(Flowable):

    def __init__(self, sub_flow):
        Flowable.__init__(self)
        self.sub_flow = sub_flow

    def draw(self):
        self.sub_flow.drawOn(self.canv, 0, 0)

    def setStyle(self, style):
        if isinstance(self.sub_flow, RotatingParagraph):
            self.sub_flow.setStyle(style)

    def wrap(self):
        return 10, 10
