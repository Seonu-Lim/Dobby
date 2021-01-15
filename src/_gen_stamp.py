from PyPDF2 import PdfFileReader
import io
from reportlab.pdfgen import canvas as cv


FILL_RGB = (255, 0, 0)
STROKE_RGB = (255, 0, 0)


def generate_stamp(x, y, code, doc_number, page_number):
    """
    Drawing the stamp with given information.
    """
    packet = io.BytesIO()
    canvas = cv.Canvas(packet, pagesize=(x, y))
    crit = float(max(x, y))
    fontsize = crit * 0.025
    canvas.setFont(
        "Courier-Bold", fontsize
    ) 
    canvas.setFillColorRGB(*FILL_RGB)
    canvas.setStrokeColorRGB(*STROKE_RGB)
    boxheight = crit * 0.0465
    if page_number < 10:
        boxwidth = crit * 0.2252 * 0.8
    elif page_number < 100:
        boxwidth = crit * 0.2527 * 0.8
    else:
        boxwidth = crit * 0.2801 * 0.8

    if x < y:  # Portrait
        position = {"x": float(x) * 0.64, "y": float(y) * 0.95203488}
    else:  # Landscape
        position = {"x": float(x) * 0.708, "y": float(y) * 0.90288714}

    canvas.rect(position["x"] * 0.99, position["y"] * 0.985, boxwidth, boxheight)
    canvas.drawString(position["x"], position["y"], f"{code}-{doc_number}-{page_number}")
    canvas.save()
    packet.seek(0)
    stamp = PdfFileReader(packet)
    return stamp.getPage(0)
