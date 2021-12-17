import cv2
import numpy as np
import os
import glob

#画像のグレースケール化（二値化していない）

def gray_scale(image):    
    color_img = cv2.imread(image)
    im_gray = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)

    cv2.imwrite(f'gray_file/{os.path.basename(image)}', im_gray)
    

#Cannyによる画像検出

def canny_filta(image):
    img = cv2.imread(image)
    img_canny = cv2.Canny(img, 100, 200)
    cv2.imwrite(f'Canny_file/{os.path.basename(image)}', img_canny)


# 動作確認用
if __name__=="__main__":
    files = glob.glob("./uploads/*")
    for file in files:
        gray_scale(file)
        canny_filta(file)
