import cv2
import numpy as np
import os

#画像のグレースケール化（二値化していない）

def gray_scale(image):    
    color_img = cv2.imread(image)
    im_gray = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)

    cv2.imwrite('gray_file/output1.jpeg', im_gray)
    

#Cannyによる画像検出

def canny_filta(image):
    img = cv2.imread(image)
    img_canny = cv2.Canny(img, 100, 200)
    cv2.imwrite('Canny_file/output2.jpeg', img_canny)
