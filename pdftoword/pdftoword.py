from pdf2docx import Converter

pdf_file = 'Ejercicio.pdf'
docx_file = 'sample2.docx'

cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()