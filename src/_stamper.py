from PyPDF2 import PdfFileReader, PdfFileWriter
import io
from reportlab.pdfgen import canvas
from _gen_stamp import *


def stamp_document(origin_path, file_name, destination_path):
    from_path = origin_path + "/" + file_name
    doc_num = file_name[:3]
    new_pdf = PdfFileReader(open(from_path, "rb"))
    n_page = new_pdf.numPages
    output = PdfFileWriter()
    for i in range(n_page):
        pageobj = new_pdf.getPage(i)
        _, _, x, y = pageobj.mediaBox
        stamp = generate_stamp(x, y, doc_num, i + 1)
        pageobj.mergePage(stamp)
        output.addPage(pageobj)
    to_path = destination_path + "/" + file_name
    outputStream = open(to_path, "wb")
    output.write(outputStream)
    outputStream.close()
