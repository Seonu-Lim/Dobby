from PyPDF2 import PdfFileReader
import io
from reportlab.pdfgen import canvas


def generate_stamp(x, y, doc_number, page_number):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=(x, y))
    crit = float(max(x, y))
    fontsize = crit * 0.025
    can.setFont(
        "Courier-Bold", fontsize
    ) 
    can.setFillColorRGB(255, 0, 0)
    can.setStrokeColorRGB(255, 0, 0)
    boxheight = crit * 0.0465
    if page_number < 10:
        boxwidth = crit * 0.2252 * 0.8
    elif page_number < 100:
        boxwidth = crit * 0.2527 * 0.8
    else:
        boxwidth = crit * 0.2801 * 0.8

    if x < y:  # Portrait
        position = (float(x) * 0.64, float(y) * 0.95203488)
    else:  # Landscape
        position = (float(x) * 0.708, float(y) * 0.90288714)

    can.rect(position[0] * 0.99, position[1] * 0.985, boxwidth, boxheight)
    can.drawString(position[0], position[1], f"3000c-{doc_number}-{page_number}")
    can.save()
    packet.seek(0)
    stamp = PdfFileReader(packet)
    return stamp.getPage(0)
