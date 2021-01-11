from PyPDF2 import PdfFileReader
import io
from reportlab.pdfgen import canvas
#from reportlab.lib.pagesizes import A4 


def generate_stamp(x, y, page_number):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=(x,y))
    can.setFont(
        "Courier-Bold", 15
    )  # TODO : Font Size also should be dependent on page size
    can.setFillColorRGB(255, 0, 0)
    can.setStrokeColorRGB(255, 0, 0)
    can.rect(
        float(x) * 0.62, float(y) * 0.89, float(x) * 0.25, float(x) * 0.05
    )  # TODO : should have flexible width, since page number varies through 1~999
    can.drawString(float(x) * 0.64, float(y) * 0.9, "3000c-111-"+str(page_number))
    can.save()
    packet.seek(0)
    stamp = PdfFileReader(packet)
    return stamp.getPage(0)
