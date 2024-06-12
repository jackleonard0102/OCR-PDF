import fitz
from PIL import Image
import pytesseract 

input_file  = 'mto_vocabulario.pdf'
pdf_file    = input_file
fullText    = ""

doc         = fitz.open(pdf_file) # open pdf files using fitz bindings 
zoom        = 5 # scale your pdf file by 120%
mat         = fitz.Matrix(zoom, zoom)
noOfPages   = doc.page_count 

for pageNo in range(noOfPages):

    page    = doc.load_page(pageNo) # number of pages
    pix     = page.get_pixmap(matrix = mat) # if you need to scale a scanned image
    output  = 'mto_vocabulario/' + str(pageNo) + '.jpg'

    pix.save(output) # skip this if you don't need to render a page



