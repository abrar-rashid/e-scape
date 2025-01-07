from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfgen import canvas
from reportlab.platypus import Frame, Paragraph

c = canvas.Canvas("test.pdf")
c.drawImage(
    "themes/images/pirate/pirate1.png",
    A4[0] * -0.125,
    A4[1] * -0.125,
    width=A4[0] * 1.25,
    height=A4[1] * 1.25,
)
c.setFont("Times-Roman", 15)
c.drawCentredString(150, 100, "hello world")

styles = getSampleStyleSheet()

styleN = styles["Normal"]
styleH = styles["Heading1"]
pirateStyle = ParagraphStyle(
    "Pirate",
    fontname="Times-Roman",
    fontSize="12")
story = []

# Positions
title_x_pos = c._pagesize[0] // 2
title_y_pos = c._pagesize[1] // 2

# add some flowables
story.append(Paragraph("This is a Heading", styleH))
story.append(
    Paragraph(
        "This is a paragraph in <i>Normal</i> style.",
        styleN))
# c  = canvas.Canvas('mydoc.pdf')

width = 6 * 25
height = 9 * 25
f = Frame(
    title_x_pos - 0.5 * width,
    c._pagesize[1] - height - 50,
    width,
    height,
    showBoundary=1,
)
f.addFromList(story, c)
# f.drawBoundary(c)

story.append(Paragraph("New paragraph", styleH))
otherFrame = Frame(200, 275, 6 * 25, 9 * 25, showBoundary=1)
otherFrame.addFromList(story, c)

c.showPage()
c.save()

# c.setFont(template.titleFont.name, template.titleFont.size)
