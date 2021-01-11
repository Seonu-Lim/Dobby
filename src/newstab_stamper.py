from PyPDF2 import PdfFileReader,PdfFileWriter
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from stamp import *

def stamp_documents(origin_path,destination_path) :
    new_pdf = PdfFileReader(open(origin_path,'rb'))
    n_page = new_pdf.numPages
    output = PdfFileWriter()
    for i in range(n_page) :
        pageobj = new_pdf.getPage(i)
        _,_,x,y = pageobj.mediaBox
        stamp = generate_stamp(x,y,i+1)
        pageobj.mergePage(stamp)
        output.addPage(pageobj)
    outputStream = open(destination_path,'wb')
    output.write(outputStream)
    outputStream.close()
    print(f'File successfully generated. Check {destination_path}.')

