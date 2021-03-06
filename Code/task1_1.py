#Import Required Libraries
from cv2 import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"




# Given Image is already in RGB, So no need of much preprocessing for our particular task
def pre_process(path):
    image = cv2.imread(path,0)
    resize_image = cv2.resize(image,(800,500))

    text = pytesseract.image_to_string(resize_image)
    print(text)
    cv2.imshow("Final Image", resize_image)
    cv2.waitKey(0)

pre_process("D:/Coding_Challenge1/Computer Vision/task1a.webp")