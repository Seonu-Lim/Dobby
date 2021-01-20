from PyPDF2 import PdfFileReader, PdfFileWriter
from _gen_stamp import *
import os


def stamp_document(code, origin_path, file_name, destination_path):
    """
    Creating & inserting stamp to the single file in the `origin_path`.
    """
    from_path = os.path.join(origin_path, file_name)
    doc_num = file_name[:3]
    new_pdf = PdfFileReader(open(from_path, "rb"),strict=False)
    n_page = new_pdf.numPages
    output = PdfFileWriter()
    for i in range(n_page):
        pageobj = new_pdf.getPage(i)
        _, _, x, y = pageobj.mediaBox
        stamp = generate_stamp(x, y, code, doc_num, i + 1)
        pageobj.mergePage(stamp)
        output.addPage(pageobj)
    to_path = os.path.join(destination_path, file_name)
    outputStream = open(to_path, "wb")
    output.write(outputStream)
    outputStream.close()
