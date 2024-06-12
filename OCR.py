import pdf2image
import fitz
import os 
import cv2

try:
    from PIL import Image
except ImportError:
    import Image
    
import pytesseract



def ocr_core(file):

    img                 = cv2.imread(file)
    gry                 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blr                 = cv2.GaussianBlur(gry, (3, 3), 0)
    thr                 = cv2.threshold(blr, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    (h_thr, w_thr)      = thr.shape[:2]
    
    s_idx               = 0
    e_idx               = int(h_thr/2)

    for _ in range(0, 2):

        crp             = thr[s_idx:e_idx, 0:w_thr]
        (h_crp, w_crp)  = crp.shape[:2]
        crp             = cv2.resize(crp, (w_crp*2, h_crp*2))
        crp             = cv2.erode(crp, None, iterations=1)
        s_idx           = e_idx
        e_idx           = s_idx + int(h_thr/2)
        text             = pytesseract.image_to_string(crp)
        
        return text


def print_pages(pdf_file):
    
    List  = [] 
    Files = os.listdir(pdf_file)
    Text  = ''

    for File in Files:
        List.append(int(File.rsplit( ".", 1 )[ 0 ]))
    
    List.sort()

    for File in List:
        Text += ocr_core(pdf_file+'/'+str(File)+'.jpg')


    f = open("/home/jake/OCR/TextFiles/mto_vocabulario.txt", "a")
    f.write(Text)
    f.close()



print_pages('/home/jake/OCR/mto_vocabulario')
