#Importing Library
from cv2 import cv2
import numpy as np

#Function
def img_masking(path):
    img = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)
    img = cv2.resize(img,(600,500))
    l_white_boundary = np.array([2, 2, 2], dtype=np.uint8)
    u_white_boundary = np.array([255, 255, 255], dtype=np.uint8)
    mask = cv2.inRange(img, l_white_boundary, u_white_boundary)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)))
    mask = cv2.bitwise_not(mask)
    
    bk = np.full(img.shape, 255, dtype=np.uint8)
    
    fg_masked = cv2.bitwise_and(img, img, mask=mask)
    
    mask = cv2.bitwise_not(mask)
    bk_masked = cv2.bitwise_and(bk, bk, mask=mask)
    final = cv2.bitwise_or(fg_masked, bk_masked)
    mask = cv2.bitwise_not(mask) 
    cv2.imshow("Final Image", final)
    cv2.waitKey(0)


# Function call
img_masking("D:/Coding_Challenge1/Computer Vision/Task-1b.png")